import pytest
from src.phone import Phone


@pytest.fixture
def phone5():
    return Phone("Samsung", 30000, 30, 2)


def test_init_phone(phone5):
    assert phone5.name == "Samsung"


def test_repr_phone(phone5):
    assert repr(phone5) == "Phone('Samsung', 30000, 30, 2)"


def test_setter_phone(phone5):
    phone5.number_of_sim = 5
    assert phone5.number_of_sim == 5
