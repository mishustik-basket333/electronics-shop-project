from src.item import Item


class Phone(Item):
    """Класс Phone, наследуется от класса Item и расширяется атрибутом 'number_of_sim'"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        self.__name = name

    def __repr__(self):
        """Метод возвращает строку в формате: 'Phone('iPhone 14', 120000, 5, 2)' """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0 and isinstance(number_of_sim, int):  # type(number_of_sim) == type(123):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
