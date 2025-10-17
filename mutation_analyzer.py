import ast
import subprocess
import os
import sys
import re

# --- Configuration --- #
# Gemini API Key - Set as environment variable for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

OUTPUT_DIR = "mutation_output"
SOURCE_TO_MUTATE_FILENAME = "source_to_mutate.py" 
TEST_FILENAME = "test_generated_mutants.py"
TRACE_FILENAME = "execution_trace.py"

# Maximum number of retry attempts for fixing test errors
MAX_RETRY_ATTEMPTS = 40

PROMPT_GENERATE_TESTS = """
Insert your test generation prompt here.
"""

PROMPT_FIX_TESTS = """
Insert your test fixing prompt here.
"""

# --- Helper Functions --- #

def create_output_directory():
    """Creates the output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def call_gemini_api(prompt_template, temperature=0.2, **kwargs):
    """Calls the Gemini API with a given prompt template, arguments, and temperature."""
    api_key = GEMINI_API_KEY
    if not api_key:
        return "Error: GEMINI_API_KEY not found in environment variables."
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        generation_config = genai.types.GenerationConfig(
            temperature=temperature
        )
        model = genai.GenerativeModel('gemini-2.0-flash', generation_config=generation_config)

        prompt = prompt_template.format(**kwargs)
        
        print(f"[INFO] Calling Gemini API (Temperature: {temperature})...")
        response = model.generate_content(prompt)
        
        if response.parts:
            code_parts = []
            for part in response.parts:
                if hasattr(part, 'text'):
                    text = part.text.strip()
                    # Clean up markdown code fences
                    if text.startswith('```python'):
                        text = text[len('```python'):].strip()
                    elif text.startswith('```'):
                        text = text[3:].strip()
                    
                    if text.endswith('```'):
                        text = text[:-3].strip()

                    if text:
                        code_parts.append(text)
            
            if not code_parts:
                return "Error: No code found in API response"
            
            print("[INFO] Gemini API call successful.")
            return "\n\n".join(code_parts)
        else:
            if response.prompt_feedback and response.prompt_feedback.block_reason:
                error_msg = f"Error: Gemini content generation blocked. Reason: {response.prompt_feedback.block_reason}"
                print(f"[ERROR] {error_msg}")
                return error_msg
            print("[WARN] Gemini API call returned no parts and no explicit block reason.")
            return "Error: Empty response from API"
            
    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {e}")
        return f"Error: {e}"

def save_code_to_file(code, filepath):
    """Saves code to a file at the specified full path."""
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        # Always use UTF-8 encoding to prevent errors on different systems
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"[INFO] Code saved to: {filepath}")
        return filepath
    except (IOError, UnicodeEncodeError) as e:
        print(f"[ERROR] Could not save code to {filepath}: {e}")
        return None

def extract_mutation_score(mutpy_output):
    """Extracts the mutation score from MutPy output."""
    # Look for mutation score in the output
    score_pattern = r"Mutation score \[.*?\]: (\d+\.\d+)%"
    match = re.search(score_pattern, mutpy_output)
    if match:
        return float(match.group(1))
    
    # Alternative pattern
    score_pattern2 = r"(\d+\.\d+)% \(\d+/\d+\)"
    match2 = re.search(score_pattern2, mutpy_output)
    if match2:
        return float(match2.group(1))
    
    return None


def run_coverage(target_file_path, test_file_path):
    """Runs pytest with coverage.py and returns the report output."""
    print(f"[INFO] Running coverage for target: {target_file_path}, tests: {test_file_path}")
    try:
        python_path = sys.executable
        target_module = os.path.splitext(os.path.basename(target_file_path))[0]
        test_filename = os.path.basename(test_file_path)
        common_dir = os.path.dirname(target_file_path)

        # Step 1: Run pytest under coverage to collect data
        run_command = [
            python_path, '-m', 'coverage', 'run', '--branch',
            f'--source={target_module}',
            '-m', 'pytest', test_filename
        ]
        
        run_process = subprocess.run(run_command, capture_output=True, text=True, cwd=common_dir)
        if run_process.returncode != 0:
            print("[WARN] Pytest execution for coverage returned a non-zero exit code.")
            print(run_process.stdout)
            print(run_process.stderr)

        # Step 2: Generate the coverage report from the collected data
        report_command = [
            python_path, '-m', 'coverage', 'report', '-m'
        ]
        
        report_process = subprocess.run(report_command, capture_output=True, text=True, cwd=common_dir)
        full_output = report_process.stdout + "\n" + report_process.stderr
        print(full_output)
        return full_output

    except Exception as e:
        print(f"[ERROR] An error occurred while running coverage: {e}")
        return f"Error: {e}"


def extract_coverage_score(coverage_output):
    """Extracts the total coverage score from the pytest-cov output."""
    # Look for the 'TOTAL' line in the coverage report
    match = re.search(r'TOTAL.*?(\d+%)', coverage_output)
    if match:
        return int(match.group(1).replace('%', ''))
    return None

def check_for_test_failures(mutpy_output):
    """Checks if there are genuine test failures in MutPy output."""
    # This regex looks for either the pytest failure summary or the MutPy pre-run failure message.
    failure_pattern = r'(==+ FAILURES ==+)|(\[\*\] Tests failed:)'
    return re.search(failure_pattern, mutpy_output) is not None

def run_mutpy(target_file_path, test_file_path):
    """Runs MutPy mutation testing and returns the mutation score and full output."""
    print(f"[INFO] Running MutPy for target: {target_file_path}, tests: {test_file_path}")
    
    try:
        # Using explicit path to mut.py script
        python_path = sys.executable  # Use current Python interpreter
        mutpy_path = os.path.join('D:\\Software\\Python\\Scripts', 'mut.py')
        
        # Get absolute paths and ensure they exist
        target_file_path = os.path.abspath(target_file_path)
        test_file_path = os.path.abspath(test_file_path)
        
        # Get the directory containing both files
        common_dir = os.path.dirname(target_file_path)
        
        # Change to the common directory
        current_dir = os.getcwd()
        os.chdir(common_dir)
        
        try:
            # Get the module names from file paths
            target_module = os.path.splitext(os.path.basename(target_file_path))[0]
            test_module = os.path.splitext(os.path.basename(test_file_path))[0]
            
            # Ensure the module names don't contain any path separators
            target_module = target_module.replace(os.sep, '_')
            test_module = test_module.replace(os.sep, '_')
            
            command = [
                python_path,
                mutpy_path,
                '--target', target_module,
                '--unit-test', test_module,
                '--runner', 'pytest'         
            ]
            
            # Execute the command
            process = subprocess.run(command, capture_output=True, text=True, cwd=common_dir)
            
        finally:
            # Change back to original directory
            os.chdir(current_dir)
        
        # Combine stdout and stderr for complete output
        full_output = process.stdout + "\n" + process.stderr
        print(full_output)
        
        # Extract mutation score
        mutation_score = extract_mutation_score(full_output)
        
        return mutation_score, full_output
        
    except Exception as e:
        print(f"[ERROR] An error occurred while running MutPy: {e}")
        return 0, f"Error: {e}"

def read_file_content(filepath):
    """Reads and returns the content of a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return ""

def get_failing_test_name(error_output):
    """
    Parses pytest or MutPy error output to find the name of the first failing test function.
    Tries multiple regex patterns to cover different output formats.
    """
    # Pattern for lines like: '.../test_generated_mutants.py::test_name'
    match = re.search(r'::(test_[a-zA-Z0-9_]+)', error_output)
    if match:
        return match.group(1)

    # Pattern for the "_____ test_name _____" header in the failure details.
    match = re.search(r'___________ (test_[a-zA-Z0-9_]+) ___________', error_output)
    if match:
        return match.group(1)
        
    # A more generic pattern as a fallback for summary lines
    match = re.search(r'FAILURES\s*.*\s*::(test_[a-zA-Z0-9_]+)', error_output)
    if match:
        return match.group(1)

    return None

def replace_function_in_code(original_code, function_name, new_function_code):
    """Replaces a function in a string of code with a new function definition using AST for precision."""
    try:
        tree = ast.parse(original_code)
        # The replacement code should be a single, valid function definition
        new_func_tree = ast.parse(new_function_code.strip())
    except (SyntaxError, ValueError) as e:
        print(f"[ERROR] Could not parse code for replacement: {e}")
        return original_code # Return original on failure

    if not (new_func_tree.body and isinstance(new_func_tree.body[0], ast.FunctionDef)):
        print(f"[ERROR] Replacement code from LLM is not a valid function definition: {new_function_code}")
        return original_code

    class FunctionReplacer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if node.name == function_name:
                print(f'[INFO] Surgically replacing function: {function_name}')
                # Return the new function node. It must be the first and only node in the parsed replacement code.
                return new_func_tree.body[0]
            return node

    transformer = FunctionReplacer()
    new_tree = transformer.visit(tree)
    return ast.unparse(new_tree)

def run_single_test_for_trace(test_filepath, failing_test_name):
    """Runs a single failing test and captures its stdout as an execution trace."""
    print(f"[INFO] Running single test to get execution trace: {failing_test_name}")
    command = [
        sys.executable,
        '-m',
        'pytest',
        f"{test_filepath}::{failing_test_name}",
        "-s"  # Disable pytest's output capture to get our print statements
    ]
    try:
        # Use a timeout to prevent hanging tests
        process = subprocess.run(command, capture_output=True, text=True, check=False, timeout=30)
        # Combine stdout and stderr so that assertion diffs (usually in stderr) are captured
        return process.stdout + "\n" + process.stderr
    except subprocess.TimeoutExpired:
        return "[TRACE-ERROR] The test timed out during trace generation."
    except Exception as e:
        return f"[TRACE-ERROR] Error running single test for trace: {e}"

def generate_and_test_with_retry(input_file):
    """Main workflow for mutation analysis."""
    print("--- Starting Mutation Analysis Workflow ---")

    # --- Step 1: Read the input file and prepare for mutation ---
    print(f"\n--- Step 1: Reading and Preparing Source File: {input_file} ---")
    try:
        with open(input_file, 'r') as f:
            full_source_code = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {input_file}: {e}")
        return

    source_to_mutate_filepath = os.path.join(OUTPUT_DIR, SOURCE_TO_MUTATE_FILENAME)
    save_code_to_file(full_source_code, source_to_mutate_filepath)
    print(f"[INFO] Source code copied to {source_to_mutate_filepath} for mutation.")

    # --- Step 2: Generate initial test cases ---
    print("\n--- Step 2: Generating initial test cases ---")
    initial_test_code = call_gemini_api(
        PROMPT_GENERATE_TESTS,
        temperature=0.2,
        source_code=full_source_code,
        source_to_mutate_filename=SOURCE_TO_MUTATE_FILENAME.replace('.py', '')
    )
    test_filepath = os.path.join(OUTPUT_DIR, TEST_FILENAME)
    save_code_to_file(initial_test_code, test_filepath)
    print(f"[INFO] Saved initial test cases to: {test_filepath}")

    current_test_code = initial_test_code
    last_error_output = ""
    failed_attempts = {}  # Memory for failed fixes, keyed by test name

    # --- Main Retry Loop ---
    for attempt in range(MAX_RETRY_ATTEMPTS):
        print(f"\n--- Step 3: Running mutation testing (Attempt {attempt + 1}/{MAX_RETRY_ATTEMPTS}) ---")
        
        exit_code, output = run_mutpy(source_to_mutate_filepath, test_filepath)

        if not check_for_test_failures(output):
            print("\n[SUCCESS] Initial tests passed. Now calculating coverage and mutation score.")
            
            print("\n--- Step 4: Calculating test coverage ---")
            coverage_output = run_coverage(source_to_mutate_filepath, test_filepath)
            coverage_score = extract_coverage_score(coverage_output)
            
            print("\n--- Step 5: Final Results ---")
            if coverage_score is not None:
                print(f"[INFO] Test Coverage: {coverage_score}%")
            else:
                print("[WARN] Could not determine test coverage.")

            mutation_score = extract_mutation_score(output)
            if mutation_score is not None:
                print(f"[INFO] Mutation Score: {mutation_score:.2f}%")
            else:
                print("[WARN] Could not determine mutation score.")

            return initial_test_code, current_test_code

        print("\n[INFO] Test failures detected. Attempting to fix...")
        last_error_output = output

        failing_test_name = get_failing_test_name(output)
        if not failing_test_name:
            # Check if this is an import-time error (no specific test failed)
            if "TypeError" in output or "NameError" in output or "AttributeError" in output:
                print("[WARN] Import-time error detected. Regenerating entire test file...")
                
                # Regenerate the entire test file with error context
                regeneration_prompt = PROMPT_GENERATE_TESTS + f"\n\n**CRITICAL: Your previous test generation caused this error during import:**\n{output}\n\nAnalyze this error carefully and generate tests that avoid this issue. Make sure all test inputs are compatible with the function's operations."
                
                new_test_code = call_gemini_api(
                    regeneration_prompt,
                    temperature=0.3,
                    source_code=full_source_code,
                    source_to_mutate_filename=SOURCE_TO_MUTATE_FILENAME.replace('.py', '')
                )
                
                if new_test_code and "Error:" not in new_test_code:
                    current_test_code = new_test_code
                    save_code_to_file(current_test_code, test_filepath)
                    print("[INFO] Regenerated test file to fix import-time error.")
                    continue
                else:
                    print("[ERROR] Failed to regenerate test file.")
                    continue
            else:
                print("[ERROR] Could not extract failing test name from output. Cannot proceed with fix.")
                continue

        if failing_test_name not in failed_attempts:
            failed_attempts[failing_test_name] = []

        attempt_context = ""
        if failed_attempts[failing_test_name]:
            attempt_context += "**IMPORTANT: You have tried the following fixes and they have FAILED. Do not repeat them. Analyze them to understand what went wrong and generate a new, different solution.**\n\n"
            for i, failed_code in enumerate(failed_attempts[failing_test_name]):
                attempt_context += f"**Failed Attempt {i + 1}:**\n```python\n{failed_code.strip()}\n```\n\n"

        temp = 0.2
        if len(failed_attempts[failing_test_name]) >= 2:
            temp = 0.4  # Get more creative after 2 failures
            print("[INFO] Increasing temperature to break loop.")

        execution_trace = run_single_test_for_trace(test_filepath, failing_test_name)

        new_function_code = call_gemini_api(
            PROMPT_FIX_TESTS,
            temperature=temp,
            failing_test_name=failing_test_name,
            source_code=full_source_code,
            test_code=current_test_code,
            error_output=output,
            execution_trace=execution_trace,
            attempt_context=attempt_context
        )

        if not new_function_code or "Error:" in new_function_code:
            print(f"[ERROR] LLM failed to generate a fix: {new_function_code}")
            continue

        failed_attempts[failing_test_name].append(new_function_code)
        current_test_code = replace_function_in_code(current_test_code, failing_test_name, new_function_code)
        save_code_to_file(current_test_code, test_filepath)

    print(f"\n[FAILURE] Could not fix the test failures after {MAX_RETRY_ATTEMPTS} attempts.")
    print("Last error output:")
    print(last_error_output)
    return initial_test_code, current_test_code



# --- Main Workflow --- #
def main(input_file):
    """The main function to orchestrate the mutation analysis process."""
    create_output_directory()
    initial_code, final_code = generate_and_test_with_retry(input_file)

    print("\n--- Analysis Finished ---")
    if final_code:
        print("Process completed. Final test code is available in the output directory.")
    else:
        print("Process halted due to errors. Please review the logs.")

if __name__ == "__main__":
    # Set your input file path here
    INPUT_FILE = "H:\\Uni work\\Thesis\\AMT\\example_input.py"  # Change this path to your actual file
    
    # Run the main workflow
    main(INPUT_FILE)