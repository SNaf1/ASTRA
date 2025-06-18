import pytest
from source_to_mutate import *

def test_empty_markdown():
    assert parse('') == '<p></p>'

def test_simple_paragraph():
    assert parse('This is a paragraph.') == '<p>This is a paragraph.</p>'

def test_h1_header():
    assert parse('# This is a header.') == '<h1>This is a header.</h1>'

def test_h2_header():
    assert parse('## This is a header.') == '<h2>This is a header.</h2>'

def test_h6_header():
    assert parse('###### This is a header.') == '<h6>This is a header.</h6>'

def test_unordered_list_single_item():
    assert parse('* Item') == '<ul><li>Item</li></ul>'

def test_unordered_list_multiple_items():
    assert parse('* Item 1\n* Item 2') == '<ul><li>Item 1</li><li>Item 2</li></ul>'

def test_paragraph_after_list():
    assert parse('* Item 1\n* Item 2\nParagraph') == '<ul><li>Item 1</li><li>Item 2</li></ul><p>Paragraph</p>'

def test_bold_text():
    assert parse('This is __bold__ text.') == '<p>This is <strong>bold</strong> text.</p>'

def test_italic_text():
    assert parse('This is _italic_ text.') == '<p>This is <em>italic</em> text.</p>'

def test_bold_and_italic_text():
    assert parse('This is __bold__ and _italic_ text.') == '<p>This is <strong>bold</strong> and <em>italic</em> text.</p>'

def test_header_with_bold_and_italic():
    assert parse('# This is __bold__ and _italic_ header.') == '<h1>This is <strong>bold</strong> and <em>italic</em> header.</h1>'

def test_list_with_bold_and_italic():
    assert parse('* This is __bold__ and _italic_ list item.') == '<ul><li>This is <strong>bold</strong> and <em>italic</em> list item.</li></ul>'

def test_mixed_content():
    markdown = '# Header\n* List item\nParagraph with __bold__ and _italic_.'
    expected = '<h1>Header</h1><ul><li>List item</li></ul><p>Paragraph with <strong>bold</strong> and <em>italic</em>.</p>'
    assert parse(markdown) == expected

def test_nested_bold_and_italic():
    assert parse('This is _a __bold and italic__ text_') == '<p>This is <em>a <strong>bold and italic</strong> text</em></p>'

def test_multiple_lines():
    markdown = 'First line\nSecond line'
    assert parse(markdown) == '<p>First line</p><p>Second line</p>'

def test_empty_lines():
    markdown = 'First line\n\nSecond line'
    assert parse(markdown) == '<p>First line</p><p></p><p>Second line</p>'

def test_header_with_leading_and_trailing_spaces():
    assert parse('  #  Header  ') == '<p>  #  Header  </p>'

def test_list_item_with_leading_and_trailing_spaces():
    assert parse('  *  List item  ') == '<p>  *  List item  </p>'

def test_paragraph_with_special_characters():
    assert parse('This is a paragraph with !@#$%^&*()_+=-`~[]\\{}|;\':",./<>? characters.') == '<p>This is a paragraph with !@#$%^&*()_+=-`~[]\\{}|;\':",./<>? characters.</p>'

def test_bold_with_special_characters():
    assert parse('__!@#$%^&*()_+=-`~[]\\{}|;\':",./<>?__') == '<p><strong>!@#$%^&*()_+=-`~[]\\{}|;\':",./<>?</strong></p>'

def test_italic_with_special_characters():
    assert parse('_!@#$%^&*()_+=-`~[]\\{}|;\':",./<>?_') == '<p>_!@#$%^&*()<em>+=-`~[]\\{}|;\':",./<>?</em></p>'

def test_header_with_number():
    assert parse('# 123') == '<h1>123</h1>'

def test_list_with_number():
    assert parse('* 123') == '<ul><li>123</li></ul>'

def test_bold_with_number():
    assert parse('__123__') == '<p><strong>123</strong></p>'

def test_italic_with_number():
    assert parse('_123_') == '<p><em>123</em></p>'

def test_header_with_hash_inside():
    assert parse('# This is a # header') == '<h1>This is a # header</h1>'

def test_list_with_asterisk_inside():
    assert parse('* This is a * list item') == '<ul><li>This is a * list item</li></ul>'

def test_bold_with_underscore_inside():
    assert parse('This is __a_bold_text__') == '<p>This is <strong>a<em>bold</em>text</strong></p>'

def test_italic_with_underscore_inside():
    assert parse('This is _an_italic_text_') == '<p>This is <em>an</em>italic<em>text</em></p>'

def test_header_level_7():
    assert parse('####### This is a header.') == '<p>####### This is a header.</p>'

def test_list_followed_by_header():
    assert parse('* Item\n# Header') == '<ul><li>Item</li></ul><h1>Header</h1>'

def test_header_followed_by_list():
    assert parse('# Header\n* Item') == '<h1>Header</h1><ul><li>Item</li></ul>'

def test_bold_at_start_of_line():
    assert parse('__bold__ text') == '<p><strong>bold</strong> text</p>'

def test_italic_at_start_of_line():
    assert parse('_italic_ text') == '<p><em>italic</em> text</p>'

def test_bold_at_end_of_line():
    assert parse('text __bold__') == '<p>text <strong>bold</strong></p>'

def test_italic_at_end_of_line():
    assert parse('text _italic_') == '<p>text <em>italic</em></p>'

def test_multiple_bold_and_italic():
    assert parse('__bold__ _italic_ __bold__ _italic_') == '<p><strong>bold</strong> <em>italic</em> <strong>bold</strong> <em>italic</em></p>'

def test_list_with_multiple_lines():
    markdown = '* Item 1\n  * Item 2'
    assert parse(markdown) == '<ul><li>Item 1</li></ul><p>  * Item 2</p>'

def test_list_with_paragraph_in_between():
    markdown = '* Item 1\nParagraph\n* Item 2'
    assert parse(markdown) == '<ul><li>Item 1</li></ul><p>Paragraph</p><ul><li>Item 2</li></ul>'

def test_list_with_empty_line_in_between():
    markdown = '* Item 1\n\n* Item 2'
    assert parse(markdown) == '<ul><li>Item 1</li></ul><p></p><ul><li>Item 2</li></ul>'

def test_bold_and_italic_in_list():
    assert parse('* __bold__ _italic_') == '<ul><li><strong>bold</strong> <em>italic</em></li></ul>'

def test_header_in_list():
    assert parse('* # Header') == '<ul><li># Header</li></ul>'

def test_list_in_header():
    assert parse('# * List') == '<h1>* List</h1>'

def test_list_with_html_tags():
    assert parse('* <li>Item</li>') == '<ul><li><li>Item</li></li></ul>'

def test_html_tags_in_paragraph():
    assert parse('<p>Paragraph</p>') == '<p><p>Paragraph</p></p>'

def test_html_tags_in_header():
    assert parse('<h1>Header</h1>') == '<h1>Header</h1>'

def test_html_tags_in_list():
    assert parse('<ul><li>Item</li></ul>') == '<ul><li><p>Item</p></li></ul>'

def test_complex_markdown():
    markdown = '# Header\n* List item 1\n* List item 2\n\nParagraph with __bold__ and _italic_.\n## Subheader'
    expected = '<h1>Header</h1><ul><li>List item 1</li><li>List item 2</li></ul><p></p><p>Paragraph with <strong>bold</strong> and <em>italic</em>.</p><h2>Subheader</h2>'
    assert parse(markdown) == expected

def test_no_wrapping_needed():
    assert parse('<ul><li>test</li></ul>') == '<ul><li><p>test</p></li></ul>'

def test_header_with_trailing_hashes():
    assert parse('## Header ##') == '<h2>Header ##</h2>'

def test_bold_with_adjacent_text():
    assert parse('text__bold__text') == '<p>text<strong>bold</strong>text</p>'

def test_italic_with_adjacent_text():
    assert parse('text_italic_text') == '<p>text<em>italic</em>text</p>'

def test_list_item_with_newline():
    assert parse('* Item\n') == '<ul><li>Item</li></ul><p></p>'

def test_list_item_with_bold_and_newline():
    assert parse('* __bold__\n') == '<ul><li><strong>bold</strong></li></ul><p></p>'

def test_list_item_with_italic_and_newline():
    assert parse('* _italic_\n') == '<ul><li><em>italic</em></li></ul><p></p>'

def test_list_item_with_multiple_lines_and_bold_italic():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_\n'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em></p><p></p>'

def test_header_with_html_entities():
    assert parse('# Header &amp;') == '<h1>Header &amp;</h1>'

def test_paragraph_with_html_entities():
    assert parse('Paragraph &amp;') == '<p>Paragraph &amp;</p>'

def test_list_item_with_html_entities():
    assert parse('* Item &amp;') == '<ul><li>Item &amp;</li></ul>'

def test_bold_with_html_entities():
    assert parse('__bold &amp;__') == '<p><strong>bold &amp;</strong></p>'

def test_italic_with_html_entities():
    assert parse('_italic &amp;_') == '<p><em>italic &amp;</em></p>'

def test_multiple_paragraphs_with_formatting():
    markdown = 'Paragraph 1 __bold__ _italic_\n\nParagraph 2 __bold__ _italic_'
    expected = '<p>Paragraph 1 <strong>bold</strong> <em>italic</em></p><p></p><p>Paragraph 2 <strong>bold</strong> <em>italic</em></p>'
    assert parse(markdown) == expected

def test_list_with_code_snippet():
    markdown = '* Item with `code`'
    assert parse(markdown) == '<ul><li>Item with `code`</li></ul>'

def test_paragraph_with_code_snippet():
    markdown = 'Paragraph with `code`'
    assert parse(markdown) == '<p>Paragraph with `code`</p>'

def test_code_snippet_with_special_characters():
    markdown = '`!@#$%^&*()`'
    assert parse(markdown) == '<p>`!@#$%^&*()`</p>'

def test_list_with_multiple_code_snippets():
    markdown = '* Item with `code1` and `code2`'
    assert parse(markdown) == '<ul><li>Item with `code1` and `code2`</li></ul>'

def test_paragraph_with_multiple_code_snippets():
    markdown = 'Paragraph with `code1` and `code2`'
    assert parse(markdown) == '<p>Paragraph with `code1` and `code2`</p>'

def test_list_with_bold_and_italic_and_code():
    markdown = '* __bold__ _italic_ `code`'
    assert parse(markdown) == '<ul><li><strong>bold</strong> <em>italic</em> `code`</li></ul>'

def test_paragraph_with_bold_and_italic_and_code():
    markdown = 'Paragraph with __bold__ _italic_ `code`'
    assert parse(markdown) == '<p>Paragraph with <strong>bold</strong> <em>italic</em> `code`</p>'

def test_list_with_newline_and_paragraph():
    markdown = '* Item\n\nParagraph'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p>Paragraph</p>'

def test_paragraph_with_newline_and_list():
    markdown = 'Paragraph\n\n* Item'
    assert parse(markdown) == '<p>Paragraph</p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_header():
    markdown = '* Item\n\n# Header'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><h1>Header</h1>'

def test_header_with_newline_and_list():
    markdown = '# Header\n\n* Item'
    assert parse(markdown) == '<h1>Header</h1><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_bold():
    markdown = '* Item\n\n__bold__'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p><strong>bold</strong></p>'

def test_bold_with_newline_and_list():
    markdown = '__bold__\n\n* Item'
    assert parse(markdown) == '<p><strong>bold</strong></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_italic():
    markdown = '* Item\n\n_italic_'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p><em>italic</em></p>'

def test_italic_with_newline_and_list():
    markdown = '_italic_\n\n* Item'
    assert parse(markdown) == '<p><em>italic</em></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_code():
    markdown = '* Item\n\n`code`'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p>`code`</p>'

def test_code_with_newline_and_list():
    markdown = '`code`\n\n* Item'
    assert parse(markdown) == '<p>`code`</p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_empty_line_and_paragraph():
    markdown = '* Item\n\n\nParagraph'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p></p><p>Paragraph</p>'

def test_paragraph_with_newline_and_empty_line_and_list():
    markdown = 'Paragraph\n\n\n* Item'
    assert parse(markdown) == '<p>Paragraph</p><p></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_empty_line_and_header():
    markdown = '* Item\n\n\n# Header'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p></p><h1>Header</h1>'

def test_header_with_newline_and_empty_line_and_list():
    markdown = '# Header\n\n\n* Item'
    assert parse(markdown) == '<h1>Header</h1><p></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_empty_line_and_bold():
    markdown = '* Item\n\n\n__bold__'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p></p><p><strong>bold</strong></p>'

def test_bold_with_newline_and_empty_line_and_list():
    markdown = '__bold__\n\n\n* Item'
    assert parse(markdown) == '<p><strong>bold</strong></p><p></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_empty_line_and_italic():
    markdown = '* Item\n\n\n_italic_'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p></p><p><em>italic</em></p>'

def test_italic_with_newline_and_empty_line_and_list():
    markdown = '_italic_\n\n\n* Item'
    assert parse(markdown) == '<p><em>italic</em></p><p></p><p></p><ul><li>Item</li></ul>'

def test_list_with_newline_and_empty_line_and_code():
    markdown = '* Item\n\n\n`code`'
    assert parse(markdown) == '<ul><li>Item</li></ul><p></p><p></p><p>`code`</p>'

def test_code_with_newline_and_empty_line_and_list():
    markdown = '`code`\n\n\n* Item'
    assert parse(markdown) == '<p>`code`</p><p></p><p></p><ul><li>Item</li></ul>'

def test_list_with_multiple_lines_and_formatting():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p>'

def test_list_with_multiple_lines_and_formatting_and_newline():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p></p>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_paragraph():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\nParagraph'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p>Paragraph</p>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_header():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n# Header'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><h1>Header</h1>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_list():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n* Item'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><ul><li>Item</li></ul>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_bold():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n__bold__'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p><strong>bold</strong></p>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_italic():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n_italic_'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p><em>italic</em></p>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_code():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n`code`'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p>`code`</p>'

def test_list_with_multiple_lines_and_formatting_and_newline_and_empty_line_and_paragraph():
    markdown = '* Line 1\n  Line 2 __bold__ _italic_ `code`\n\n\nParagraph'
    assert parse(markdown) == '<ul><li>Line 1</li></ul><p>  Line 2 <strong>bold</strong> <em>italic</em> `code`</p><p></p><p></p><p>Paragraph</p>'