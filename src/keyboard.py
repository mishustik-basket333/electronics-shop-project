from src.item import Item


class MixinLanguage:
    """Mixin class"""

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод """
        if self.__language == "RU":
            self.__language = "EN"
            return self
        elif self.__language == "EN":
            self.__language = "RU"
            return self


class Keyboard(Item, MixinLanguage):
    """Класс Keyboard"""
    pass
