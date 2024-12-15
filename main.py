from abc import ABC, abstractmethod
from typing import List, Optional

class Table(ABC):
    """
    Абстрактный класс, описывающий объект "Стол".
    """

    def __init__(self, material: str, legs: int):
        """
        Инициализация стола.

        :param material: Материал, из которого сделан стол (древесина, металл и т.д.)
        :param legs: Количество ножек стола. Должно быть больше или равно 1.
        :raises ValueError: Если количество ножек меньше 1.
        """
        if legs < 1:
            raise ValueError("Количество ножек должно быть >= 1")
        self.material = material
        self.legs = legs

    @abstractmethod
    def assemble(self) -> None:
        """
        Метод для сборки стола.
        """
        ...

    @abstractmethod
    def move(self, new_position: str) -> None:
        """
        Переместить стол в новое положение.

        :param new_position: Новое местоположение стола.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий объект "Дерево".
    """

    def __init__(self, species: str, height: float):
        """
        Инициализация дерева.

        :param species: Вид дерева (дуб, сосна и т.д.).
        :param height: Высота дерева в метрах. Должна быть положительным числом.
        :raises ValueError: Если высота <= 0.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0")
        self.species = species
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличить высоту дерева на основе его возраста.

        :param years: Количество лет, за которое дерево растёт. Должно быть >= 1.
        """
        ...

    @abstractmethod
    def photosynthesize(self) -> str:
        """
        Выполняет процесс фотосинтеза и возвращает статус.

        :return: Статус процесса фотосинтеза.
        """
        ...


class SocialMediaPlatform(ABC):
    """
    Абстрактный класс, описывающий социальную медиа-платформу.
    """

    def __init__(self, name: str, users: int):
        """
        Инициализация социальной платформы.

        :param name: Название платформы.
        :param users: Количество зарегистрированных пользователей. Должно быть >= 0.
        :raises ValueError: Если количество пользователей меньше 0.
        """
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.name = name
        self.users = users

    @abstractmethod
    def post_content(self, content: str) -> None:
        """
        Размещает контент на платформе.

        :param content: Текст или мультимедийный контент для публикации.
        """
        ...

    @abstractmethod
    def add_user(self, username: str) -> None:
        """
        Добавляет нового пользователя на платформу.

        :param username: Имя нового пользователя.
        """
        ...

    @abstractmethod
    def generate_report(self) -> str:
        """
        Создаёт отчёт о текущем состоянии платформы.

        :return: Строка с данными отчёта.
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
