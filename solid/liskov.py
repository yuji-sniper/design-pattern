# リスコフの置換原則（Liskov Substitution Principle）

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self):
        self.__width = 0
        self.__height = 0
    
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float) -> None:
        self.__width = width
    
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float) -> None:
        self.__height = height
    
    def area(self) -> float:
        return self.__width * self.__height


class Square(Shape):
    def __init__(self):
        self.__side = 0
    
    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, side: float) -> None:
        self.__side = side
    
    def area(self) -> float:
        return self.__side ** 2


def f(shape: Shape) -> None:
    print(shape.area())


if __name__ == "__main__":
    r1 = Rectangle()
    r1.width = 5
    r1.height = 10
    f(r1)
    
    r2 = Square()
    r2.side = 5
    f(r2)
