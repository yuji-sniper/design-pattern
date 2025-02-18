# Decorator pattern

'''
継承による機能追加は不要な機能も継承してしまうため、
Decoratorパターンを使って柔軟に動的に機能を追加することができる。

- メリット
    - 実行時の機能追加が容易にできる
    - 複数の機能を組み合わせることができる
- デメリット
    - 組み合わせた機能から特定の機能の削除が難しい
    - 振る舞いがデコレーターの組み合わせの順番に依存する
- 使いどころ
    - 追加したい機能のパターンが複数ある場合
    - 追加したい機能のパターンに順序がある場合
    - 継承を使ってオブジェクトの機能拡張が困難な場合
        - 例: finalクラスの場合
'''

import datetime
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class Logger(Component):
    def get_log_message(self, msg: str) -> str:
        return msg


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class TimeStampDecorator(Decorator):
    def __init__(self, component: Component):
        super().__init__(component)
    
    def get_log_message(self, msg: str) -> str:
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        return self._component.get_log_message(f'{timestamp} {msg}')

class LevelDecorator(Decorator):
    def __init__(self, component: Component, level: str):
        super().__init__(component)
        self.__level = level
    
    def get_log_message(self, msg: str) -> str:
        return self._component.get_log_message(f'[{self.__level}] {msg}')


if __name__ == '__main__':
    logger = Logger()
    logger = TimeStampDecorator(logger)
    logger = LevelDecorator(logger, 'INFO')

    print(logger.get_log_message('Hello, World!'))
    # 2021-10-17 14:23:24 [INFO] [DEBUG] Hello, World!
