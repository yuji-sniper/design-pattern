# オープン・クローズドの原則（Open/Closed Principle）

import math
from abc import ABCMeta, abstractmethod


class IEmployee(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass


class JuniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)
    
    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.1)


class MiddleEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)
    
    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.2)


class SeniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)
    
    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.3)


# 拡張
class ExpertEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)
    
    def get_bonus(self, base: int) -> int:
        return math.floor(base * 3)


if __name__ == "__main__":
    emp1 = JuniorEmployee("Taro")
    emp2 = MiddleEmployee("Jiro")
    emp3 = SeniorEmployee("Saburo")
    emp4 = ExpertEmployee("Shiro")
    
    base = 100
    print(f"{emp1.name}: {emp1.get_bonus(base)}")
    print(f"{emp2.name}: {emp2.get_bonus(base)}")
    print(f"{emp3.name}: {emp3.get_bonus(base)}")
    print(f"{emp4.name}: {emp4.get_bonus(base)}")
