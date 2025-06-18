# ASTRA: Automated Software Test Repair and Analysis

ASTRA is a Python-based framework that leverages Large Language Models (LLMs) to automate the entire lifecycle of unit testing: from generation and evaluation to autonomous repair. It is designed to create robust test suites that achieve high mutation and coverage scores with minimal human intervention.

## Overview

The primary goal of ASTRA is to address the high cost and time consumption associated with writing and maintaining unit tests. It uses the Google Gemini API to intelligently generate and fix `pytest` tests for a given Python source file, creating a self-healing system that adapts to code changes and test failures.

## Features

- **Automated Test Generation**: Creates comprehensive `pytest` test suites from a Python source file.
- **Autonomous Test Repair**: If tests fail during mutation testing, ASTRA identifies the root cause, captures a dynamic execution trace, and uses an LLM to surgically repair the failing test function.
- **Mutation Testing Integration**: Uses `mutpy` to run mutation analysis and provides a final mutation score as a key quality metric.
- **Coverage Analysis**: Measures branch coverage of the generated tests using `coverage.py`.
- **Surgical AST-Based Fixes**: Replaces only the broken test function using Abstract Syntax Trees (AST), preserving the integrity of the rest of the test suite.

## Workflow

The framework operates in a sequential, automated workflow:

1.  **Input**: Takes a single Python source file as input.
2.  **Test Generation**: Calls the Gemini API with a sophisticated prompt to generate an initial set of `pytest` tests.
3.  **Mutation Analysis**: Executes `mutpy` to run mutation testing against the generated tests.
4.  **Failure Detection**: If `mutpy` reports test failures, the framework enters a repair loop.
5.  **Repair Loop**:
    a. The name of the first failing test is extracted from the error log.
    b. The single failing test is re-run to capture a precise execution trace.
    c. The LLM is called with a specialized "fix" prompt, providing the source code, the broken test, the error traceback, and the execution trace.
    d. The LLM returns a corrected version of the test function.
    e. The old function is surgically replaced with the new one using AST manipulation.
    f. The loop repeats by re-running `mutpy`.
6.  **Success**: Once all tests pass, the framework calculates and reports the final mutation score and branch coverage.

## Setup and Configuration

To replicate this project and run the tool, you must perform the following configuration steps:

1.  **Install Dependencies**: Install all required packages using pip.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set Your API Key**: Open `mutation_analyzer.py` and replace the empty string in the `GEMINI_API_KEY` variable with your own Google Gemini API key.
    ```python
    # mutation_analyzer.py
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```

3.  **Add Your Prompts**: In `mutation_analyzer.py`, paste your custom prompts into the `PROMPT_GENERATE_TESTS` and `PROMPT_FIX_TESTS` variables. The placeholders inside the prompt strings must be kept intact.

4.  **Update MutPy Path**: The script contains a hardcoded path to the `mut.py` executable. You **must** change this to match the location of the `Scripts` folder in your Python installation.
    ```python
    # mutation_analyzer.py
    # Find this line and update the path
    mutpy_path = os.path.join('D:\\Software\\Python\\Scripts', 'mut.py') 
    ```

## How to Run

1.  Place the Python file you want to test into the root directory of the project.
2.  Open `mutation_analyzer.py` and update the `INPUT_FILE` variable to point to your target file.
    ```python
    # mutation_analyzer.py
    INPUT_FILE = "path/to/your/file.py"
    ```
3.  Run the script from your terminal:
    ```bash
    python mutation_analyzer.py
    ```

The tool will create a `mutation_output` directory containing the source file to be mutated and the generated/repaired test file.
