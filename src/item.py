import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        try:
            with open('items.csv', "r", encoding='windows-1251') as csv_file:
                data = csv.reader(csv_file)
                for raw in data:
                    try:
                        InstantiateCSVError(raw)
                    except InstantiateCSVErrorPost as e:
                        print(e)
                        raise InstantiateCSVErrorPost("Файл item.csv поврежден")
                    break

                for raw in data:
                    if raw[0] == "name":
                        continue
                    else:
                        Item(raw[0], float(raw[1]), int(raw[2]))
        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")

    @staticmethod
    def string_to_number(number_in_str):
        """Статический метод, возвращающий число из числа-строки"""
        number = int(float(number_in_str))
        return number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """"""
        if not isinstance(other, Item):
            raise "Складывать можно только объекты Item и дочерние от них."
        data = int(self.quantity + other.quantity)
        return data


# class InstantiateCSVError(Exception):
#     """Общий класс"""


class InstantiateCSVErrorPost(Exception):
    """Нет одной из колонок в данных"""
    def __init__(self, *args):
        self.msg = args[0] if args else None

    def __str__(self):
        return self.msg


class InstantiateCSVError:
    """Класс для работы с данными"""

    def __init__(self, data):
        if len(data) != 3:
            raise InstantiateCSVErrorPost("Неправильное количество столбцов")
        else:
            self.data = data
