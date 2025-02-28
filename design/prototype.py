# Prototype pattern

'''
- メリット
    - オブジェクトの生成処理を隠蔽できる。
    - 構築済みのプロトタイプのクローンの作成を使うことで、
      初期化コードの重複を削減。
    - 利用者と具体的なクラスの結合度を弱められる。

- デメリット
    - ディープコピーとシャローコピーを意識しないと
      想定外のバグを生む可能性がある。

- 使いどころ
    - クラスからのインスタンス生成が難しい場合。
    - 例）ユーザー操作によって生成された
          パワポの図形オブジェクトなど
'''

from __future__ import annotations
import copy
from abc import ABCMeta, abstractmethod


class ItemPrototype(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.__name = name
        self.__review: list[str] = []
    
    def __str__(self) -> str:
        return f"{self.__name}: {self.__review}"
    
    def set_review(self, review: str) -> None:
        self.__review.append(review)
    
    @abstractmethod
    def create_copy(self) -> ItemPrototype:
        pass


class DeepCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.deepcopy(self)

class ShallowCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.copy(self)


class ItemManager:
    def __init__(self):
        self.items = {}
    
    def register_item(self, key: str, item: ItemPrototype) -> None:
        self.items[key] = item
    
    def create(self, key: str):
        if key in self.items:
            item = self.items[key]
            return item.create_copy()
        raise Exception(f"{key} is not registered.")


if __name__ == "__main__":
    mouse = DeepCopyItem("マウス")
    keyboard = ShallowCopyItem("キーボード")
    
    manager = ItemManager()
    manager.register_item("mouse", mouse)
    manager.register_item("keyboard", keyboard)
    
    copy_mouse = manager.create("mouse")
    copy_keyboard = manager.create("keyboard")
    
    copy_mouse.set_review("使いやすい")
    copy_keyboard.set_review("打ちやすい")
    
    print(mouse)
    print(copy_mouse) # ディープコピーなので、レビューがコピーされている
    print()
    print(keyboard)
    print(copy_keyboard) # シャローコピーなので、レビューがコピーされていない
