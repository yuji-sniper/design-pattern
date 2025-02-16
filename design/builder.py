# Builder pattern

'''
- メリット
    - 生成されるオブジェクトの生成過程や
      生成手順を隠蔽できる。
    - オブジェクト構築用のコードを
      ビジネスロジックから分離できる。

- 使いどころ
    - 生成手順が同じで、詳細が異なるオブジェクトを生成する場合。
    - 大量のパラメータをコンストラクタに渡して
      オブジェクトを生成している場合。
      - Builderの各工程で必要なパラメータのみ渡すことで、
        パラメータを小分けにして渡すことができるため、
        コードの可読性が向上する。
'''

from abc import ABCMeta, abstractmethod


class Computer:
    def __init__(self):
        self.type = None
        self.cpu = None
        self.ram = None
    
    def __str__(self) -> str:
        return f"type: {self.type}, cpu: {self.cpu}, ram: {self.ram}"


class ComputerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_cpu(self, cpu: str):
        pass
    
    @abstractmethod
    def add_ram(self, ram: str):
        pass


class DesktopBuilder(ComputerBuilder):
    def __init__(self):
        self.__computer = Computer()
        self.__computer.type = "Desktop"
    
    def add_cpu(self, cpu: str):
        self.__computer.cpu = cpu
    
    def add_ram(self, ram: str):
        self.__computer.ram = ram
    
    def get_result(self) -> Computer:
        return self.__computer

class LaptopBuilder(ComputerBuilder):
    def __init__(self):
        self.__computer = Computer()
        self.__computer.type = "Laptop"
    
    def add_cpu(self, cpu: str):
        self.__computer.cpu = cpu
    
    def add_ram(self, ram: str):
        self.__computer.ram = ram
    
    def get_result(self) -> Computer:
        return self.__computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.__builder = builder
    
    def construct(self):
        self.__builder.add_cpu("Intel Core i7")
        self.__builder.add_ram("16GB")

    def high_spec_construct(self):
        self.__builder.add_cpu("M2")
        self.__builder.add_ram("32GB")


if __name__ == "__main__":
    desktop_builder = DesktopBuilder()
    desktop_director = Director(desktop_builder)
    desktop_director.construct()
    desktop = desktop_builder.get_result()
    print(desktop)
    
    laptop_builder = LaptopBuilder()
    laptop_director = Director(laptop_builder)
    laptop_director.high_spec_construct()
    laptop = laptop_builder.get_result()
    print(laptop)
