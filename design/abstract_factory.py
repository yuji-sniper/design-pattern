# Abstract Factory Pattern

'''
- メリット
    - 具体的なクラスをクライアントから隠蔽できる。
    - 利用する部品群の整合性を保つことができる。

- 使いどころ
    - 関連する部品群を決められた種別ごとに
      整合性を保って切り替えたい場合。

- Factory Methodとの違い
    - 生成するインスタンスの数
        - Factory Method: 1つのインスタンスを生成
        - Abstract Factory: 複数の部品セットを生成
    - 抽象化の対象
        - Factory Method: メソッド
        - Abstract Factory: クラス（インターフェース）
'''

from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self):
        pass

class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsButton(Button):
    def press(self):
        print('Windows button pressed')

class WindowsCheckbox(Checkbox):
    def switch(self):
        print('Windows checkbox switched')


class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacButton(Button):
    def press(self):
        print('Mac button pressed')

class MacCheckbox(Checkbox):
    def switch(self):
        print('Mac checkbox switched')


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def run(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.press()
    checkbox.switch()


if __name__ == '__main__':
    run(WindowsGUIFactory())
    run(MacGUIFactory())
