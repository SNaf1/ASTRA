import pytest
from source_to_mutate import handle_error_by_throwing_exception, handle_error_by_returning_none, handle_error_by_returning_tuple, filelike_objects_are_closed_on_exception

def test_handle_error_by_throwing_exception():
    with pytest.raises(Exception) as excinfo:
        handle_error_by_throwing_exception()
    assert str(excinfo.value) == 'Meaningful message describing the source of the error'

def test_handle_error_by_returning_none_valid_input():
    assert handle_error_by_returning_none("123") == 123

def test_handle_error_by_returning_none_invalid_input():
    assert handle_error_by_returning_none("abc") is None

def test_handle_error_by_returning_tuple_valid_input():
    assert handle_error_by_returning_tuple("456") == (True, 456)

def test_handle_error_by_returning_tuple_invalid_input():
    assert handle_error_by_returning_tuple("def") == (False, None)

class MockFilelikeObject:
    def __init__(self):
        self.closed = False
        self.something_done = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True

    def do_something(self):
        raise Exception("Simulated exception")

def test_filelike_objects_are_closed_on_exception():
    mock_file = MockFilelikeObject()
    with pytest.raises(Exception, match="Simulated exception"):
        filelike_objects_are_closed_on_exception(mock_file)
    assert mock_file.closed is True