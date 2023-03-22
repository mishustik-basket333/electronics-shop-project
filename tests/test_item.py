"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item3():
    return Item("Холодильник", 30000, 30)


@pytest.fixture
def item4():
    return Item("Пылесос", 5_000, 9)


def test_calculate_total_price(item3, item4):
    """Рассчитывает общую стоимость конкретного товара в магазине. Возвращает общую стоимость товара"""
    assert item3.calculate_total_price() == 900_000
    assert item4.calculate_total_price() == 45_000


def test_apply_discount(item3, item4):
    """Применяет установленную скидку для конкретного товара"""
    item3.pay_rate = 0.5
    item3.apply_discount()
    assert item3.price == 15_000

    item4.pay_rate = 0.8
    item4.apply_discount()
    assert item4.price == 4_000


def test__init__(item3):
    """Проверяет соответствие имени конкретного экземпляра"""
    assert item3.name == "Холодильник"


def test_string_to_number():
    """Статический метод, возвращающий число из числа-строки"""
    assert Item.string_to_number("9") == 9
    assert Item.string_to_number("1.5") == 1


def test_repr(item4):
    assert repr(item4) == "Item('Пылесос', 5000, 9)"


def test_str(item3):
    assert str(item3) == "Холодильник"


def test_add_item(item3, item4):
    assert item4 + item3 == 39
