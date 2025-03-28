from typing import List, Optional


class Shape:
    """
    Базовый класс для геометрических фигур.

    Args:
        name (str): Название фигуры.
        color (str): Цвет фигуры.
    """

    def __init__(self, name: str, color: str) -> None:
        """
        Инициализирует объект Shape.
        """
        self.name = name
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Shape.
        """
        return f"{self.name} ({self.color})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Shape для отладки.
        """
        return f"Shape(name='{self.name}', color='{self.color}')"

    def area(self) -> float:
        """
        Вычисляет площадь фигуры.  В базовом классе возвращает 0,
        так как площадь зависит от конкретного типа фигуры.
        """
        return 0.0

    def describe(self) -> str:
        """
        Возвращает описание фигуры.
        """
        return f"Это {self.name} цвета {self.color}."


class Rectangle(Shape):
    """
    Дочерний класс для прямоугольника, наследуется от Shape.

    Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
        color (str): Цвет прямоугольника.
    """

    def __init__(self, width: float, height: float, color: str) -> None:
        """
        Инициализирует объект Rectangle, расширяя конструктор Shape.
        """
        super().__init__("Rectangle", color)
        self.width = width
        self.height = height
        # _perimeter - приватный атрибут, так как он вычисляется на основе ширины и высоты,
        # и нет смысла позволять пользователю менять его напрямую.
        self._perimeter: Optional[float] = None

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Rectangle.
        Перегружает метод базового класса для добавления информации о размерах.
        """
        return f"{super().__str__()} (width={self.width}, height={self.height})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Rectangle для отладки.
        Перегружает метод базового класса для добавления информации о размерах.
        """
        return f"Rectangle(width={self.width}, height={self.height}, color='{self.color}')"

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.
        Перегружает метод базового класса для реализации логики вычисления площади прямоугольника.
        """
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника.  Результат сохраняется в приватном атрибуте _perimeter.

        # Инкапсуляция: _perimeter - приватный атрибут, так как доступ к нему должен осуществляться только через методы класса.
        """
        self._perimeter = 2 * (self.width + self.height)
        return self._perimeter

    def get_perimeter(self) -> float:
        """
        Возвращает периметр прямоугольника.
        Если периметр еще не вычислен, то вычисляет его.
        """
        if self._perimeter is None:
            self.calculate_perimeter()
        return self._perimeter

    def describe(self, include_area: bool = False) -> str:
        """
        Возвращает описание прямоугольника, включая его площадь, если include_area=True.
        Перегружает метод базового класса для добавления информации о размерах и площади.

        Args:
            include_area (bool):  Флаг, указывающий, нужно ли включать площадь в описание.
        """
        description = f"{super().describe()} Это прямоугольник шириной {self.width} и высотой {self.height}."
        if include_area:
            description += f" Его площадь равна {self.area()}."
        return description

    def is_square(self) -> bool:
        """
        Проверяет, является ли прямоугольник квадратом.
        """
        return self.width == self.height


if __name__ == "__main__":
    # Пример использования классов
    shape = Shape("Generic Shape", "Gray")
    print(shape)  # Generic Shape (Gray)
    print(repr(shape))  # Shape(name='Generic Shape', color='Gray')
    print(shape.area())  # 0.0
    print(shape.describe()) # Это Generic Shape цвета Gray.

    rectangle = Rectangle(5.0, 10.0, "Blue")
    print(rectangle)  # Rectangle (Blue) (width=5.0, height=10.0)
    print(repr(rectangle))  # Rectangle(width=5.0, height=10.0, color='Blue')
    print(rectangle.area())  # 50.0
    print(rectangle.describe()) # Это Rectangle цвета Blue. Это прямоугольник шириной 5.0 и высотой 10.0.
    print(rectangle.describe(include_area=True)) # Это Rectangle цвета Blue. Это прямоугольник шириной 5.0 и высотой 10.0. Его площадь равна 50.0.
    print(rectangle.is_square())  # False
    print(rectangle.calculate_perimeter())
    print(rectangle.get_perimeter())