'''Создать абстрактный класс Figure (на плоскости) с методами вычисления площа-ди и периметра, а также методом, выводящим информацию о фигуре на экран. 
Создать подклассы: Rectangle (прямоугольник), Circle (круг), Triangle (треугольник) со своими методами вычисления площади и периметра.
Создать список из n фигур и вывести полную информацию о фигурах на экран.'''



import math
from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        """
         Метод для вычисления площади фигуры.
.
        """
        pass  # Метод должен быть реализован в подклассах

    @abstractmethod
    def calculate_perimeter(self):
        """
        Абстрактный метод для вычисления периметра фигуры.

        """
        pass  # Метод должен быть реализован в подклассах

    def display_info(self):

        print(f"Тип фигуры: {self.__class__.__name__}")  # Выводим имя класса
        print(f"Площадь: {self.calculate_area():.2f}") # Округляем до двух знаков после запятой
        print(f"Периметр: {self.calculate_perimeter():.2f}")
        print("-" * 20) # Разделитель между фигурами


class Rectangle(Figure):
    """
    Класс Rectangle, представляющий прямоугольник.
    """

    def __init__(self, width, height):
        """
        Конструктор класса.

        """
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Вычисление площади прямоугольника.

        """
        return self.width * self.height

    def calculate_perimeter(self):
        """
        Вычисление периметра прямоугольника.

        """
        return 2 * (self.width + self.height)


class Circle(Figure):
    """
    Класс Circle, представляющий круг.
    """

    def __init__(self, radius):
        """
        Конструктор класса.

        """
        self.radius = radius

    def calculate_area(self):
        """
        Вычисление площади круга.

        """
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        """
        Вычисление периметра круга (длины окружности).

        """
        return 2 * math.pi * self.radius


class Triangle(Figure):
    """
    Класс Triangle, представляющий треугольник.

    """

    def __init__(self, side):
        """
        Конструктор класса.

        """
        self.side = side

    def calculate_area(self):
        """
        Вычисление площади равностороннего треугольника.

        """
        return (math.sqrt(3) / 4) * self.side**2  # Формула площади равностороннего треугольника

    def calculate_perimeter(self):
        """
        Вычисление периметра треугольника.

        """
        return 3 * self.side


# Создание списка фигур
n = 3  # Количество фигур
figures = []

figures.append(Rectangle(width=5, height=10))
figures.append(Circle(radius=3))
figures.append(Triangle(side=4))


# Вывод информации о фигурах
for figure in figures:
    figure.display_info()