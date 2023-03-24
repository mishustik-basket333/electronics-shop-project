import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_1():
    return Keyboard("Samsung_keyboard_001", 3000, 30)


def test_init_keyboard(keyboard_1):
    assert keyboard_1.language == "EN"


def test_change_lang_keyboard(keyboard_1):
    keyboard_1.change_lang()
    assert keyboard_1.language == "RU"
    keyboard_1.change_lang()
    assert keyboard_1.language == "EN"
