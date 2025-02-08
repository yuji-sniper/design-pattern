# インターフェース分離の原則

from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Movable(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class Flyable(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Airplane(Vehicle, Movable, Flyable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
    
    def start(self):
        print(f'{self.color}の{self.name}が飛び立ちました。')
    
    def stop(self):
        print(f'{self.color}の{self.name}が着陸しました。')
    
    def fly(self):
        print(f'{self.color}の{self.name}が飛行中です。')


class Car(Vehicle, Movable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)
    
    def start(self):
        print(f'{self.color}の{self.name}が走り出しました。')
    
    def stop(self):
        print(f'{self.color}の{self.name}が停車しました。')


if __name__ == '__main__':
    airplane = Airplane('ボーイング747', '白')
    airplane.start()
    airplane.fly()
    airplane.stop()
    
    car = Car('トヨタ', '赤')
    car.start()
    car.stop()
