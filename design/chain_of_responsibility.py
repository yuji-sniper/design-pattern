# Chain of Responsibility Pattern

'''
- メリット
    - リクエスト処理の順序を制御できる
    - リクエストの送信側と受信側の結合を緩和できる
    - 新しい処理クラスを容易に追加できる
- デメリット
    - 処理がたらい回しにされるので、
      パフォーマンスに影響が出る可能性がある
- 使いどころ
    - 特定の順序で複数の処理を実行する必要がある場合
    - 例）
        - フォーム入力値のバリデーション
'''

from __future__ import annotations
import re
from abc import ABCMeta, abstractmethod


class ValidationHandler(metaclass=ABCMeta):
    def __init__(self):
        self.__next_handler = None
    
    def set_handler(self, handler: ValidationHandler) -> ValidationHandler:
        self.__next_handler = handler
        return handler

    @abstractmethod
    def _exec_validation(self, value: str) -> bool:
        pass

    @abstractmethod
    def _get_error_message(self):
        pass
    
    def validate(self, value: str) -> bool:
        result = self._exec_validation(value)
        
        if not result:
            self._get_error_message()
            return False
        elif self.__next_handler:
            return self.__next_handler.validate(value)
        else:
            return True


class NotNullValidationHandler(ValidationHandler):
    def _exec_validation(self, value: str) -> bool:
        result = (value != '')
        return result

    def _get_error_message(self):
        print('入力してください')

class AlphabetValidationHandler(ValidationHandler):
    def _exec_validation(self, value: str) -> bool:
        result = bool(re.match(r'^[a-zA-Z]+$', value))
        return result

    def _get_error_message(self):
        print('半角英字で入力してください')

class MinLengthValidationHandler(ValidationHandler):
    def _exec_validation(self, value: str) -> bool:
        result = (len(value) >= 4)
        return result

    def _get_error_message(self):
        print('4文字以上で入力してください')


if __name__ == '__main__':
    not_null_handler = NotNullValidationHandler()
    alphabet_handler = AlphabetValidationHandler()
    min_length_handler = MinLengthValidationHandler()
    
    validation_handlers = [
        not_null_handler,
        alphabet_handler,
        min_length_handler
    ]
    
    first_handler = validation_handlers[0]
    current_handler = validation_handlers[0]
    
    for handler in validation_handlers[1:]:
        current_handler.set_handler(handler)
        current_handler = handler
    
    test_values = ["", "123", "abc", "abcd", "abcdef"]

    for value in test_values:
        print('value: ', value)
        result = first_handler.validate(value)
        print('result: ', result)
        print()
