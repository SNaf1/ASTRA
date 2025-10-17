import pytest
from selected_functions import *

@pytest.fixture(autouse=True)
def reset_state():
    import selected_functions
    if hasattr(selected_functions, 'c'):
        selected_functions.c.happy_level = 0
        selected_functions.c.eyes_crossed = False
        selected_functions.c.tongue_out = False

def test_hide_happy(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 100, 'y': 100})() # Dummy event object
    hide_happy(event)

def test_sad_happy_level_zero(monkeypatch):
    # Mock c.itemconfigure and root.after to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    def mock_after(delay, callback):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    monkeypatch.setattr("selected_functions.root.after", mock_after)
    c.happy_level = 0
    sad()

def test_sad_happy_level_positive(monkeypatch):
    # Mock c.itemconfigure and root.after to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    def mock_after(delay, callback):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    monkeypatch.setattr("selected_functions.root.after", mock_after)
    c.happy_level = 5
    sad()
    assert c.happy_level == 4

def test_show_happy_within_range(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 100, 'y': 100})() # Dummy event object
    show_happy(event)
    assert c.happy_level == 10

def test_show_happy_outside_range_x_low(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 10, 'y': 100})() # Dummy event object
    show_happy(event)
    assert c.happy_level == 0

def test_show_happy_outside_range_x_high(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 400, 'y': 100})() # Dummy event object
    show_happy(event)
    assert c.happy_level == 0

def test_show_happy_outside_range_y_low(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 100, 'y': 10})() # Dummy event object
    show_happy(event)
    assert c.happy_level == 0

def test_show_happy_outside_range_y_high(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    event = type('obj', (object,), {'x': 100, 'y': 400})() # Dummy event object
    show_happy(event)
    assert c.happy_level == 0

def test_toggle_eyes(monkeypatch):
    # Mock c.itemcget and c.itemconfigure to avoid actual GUI calls
    def mock_itemcget(item, option):
        if item in [eye_left, eye_right]:
            return 'white' # Initial state
        elif item in [pupil_left, pupil_right]:
            return HIDDEN
        return None

    def mock_itemconfigure(item, state=None, fill=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemcget", mock_itemcget)
    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)

    toggle_eyes()

def test_toggle_pupils_eyes_not_crossed(monkeypatch):
    # Mock c.move to avoid actual GUI calls
    def mock_move(item, x, y):
        pass

    monkeypatch.setattr("selected_functions.c.move", mock_move)
    c.eyes_crossed = False
    toggle_pupils()
    assert c.eyes_crossed == True

def test_toggle_pupils_eyes_crossed(monkeypatch):
    # Mock c.move to avoid actual GUI calls
    def mock_move(item, x, y):
        pass

    monkeypatch.setattr("selected_functions.c.move", mock_move)
    c.eyes_crossed = True
    toggle_pupils()
    assert c.eyes_crossed == False

def test_toggle_tongue_tongue_not_out(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    c.tongue_out = False
    toggle_tongue()
    assert c.tongue_out == True

def test_toggle_tongue_tongue_out(monkeypatch):
    # Mock c.itemconfigure to avoid actual GUI calls
    def mock_itemconfigure(item, state=None):
        pass

    monkeypatch.setattr("selected_functions.c.itemconfigure", mock_itemconfigure)
    c.tongue_out = True
    toggle_tongue()
    assert c.tongue_out == False

def test_cheeky(monkeypatch):
    # Mock toggle_tongue, toggle_pupils, hide_happy, and root.after
    def mock_toggle_tongue():
        pass

    def mock_toggle_pupils():
        pass

    def mock_hide_happy(event):
        pass

    def mock_after(delay, callback):
        pass

    monkeypatch.setattr("selected_functions.toggle_tongue", mock_toggle_tongue)
    monkeypatch.setattr("selected_functions.toggle_pupils", mock_toggle_pupils)
    monkeypatch.setattr("selected_functions.hide_happy", mock_hide_happy)
    monkeypatch.setattr("selected_functions.root.after", mock_after)

    event = type('obj', (object,), {'x': 100, 'y': 100})()
    cheeky(event)

def test_blink(monkeypatch):
    # Mock toggle_eyes and root.after
    def mock_toggle_eyes():
        pass

    def mock_after(delay, callback):
        pass

    monkeypatch.setattr("selected_functions.toggle_eyes", mock_toggle_eyes)
    monkeypatch.setattr("selected_functions.root.after", mock_after)

    blink()