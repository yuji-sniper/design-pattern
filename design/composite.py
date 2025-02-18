# Composite pattern

'''
- メリット
    - 複雑なツリー構造を簡単に扱うことができる
    - 新しい枝葉を簡単に追加できる
- デメリット
    - 枝と葉の機能が大きく異なる場合、
      共通のAPIを作ることが困難
- 使いどころ
    - 再帰的なツリー構造を扱う場合
    - 例）
        - ディレクトリツリー、組織階層、DOMツリー
'''

from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_size(self) -> int:
        pass
    
    @abstractmethod
    def remove(self):
        pass


class File(Entry):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.__size = size
    
    def get_size(self) -> int:
        return self.__size
    
    def remove(self):
        print(f'{self.name}を削除しました')

class Directory(Entry):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children: list[Entry] = []
    
    def get_size(self) -> int:
        size = 0
        for child in self.__children:
            size += child.get_size()
        return size
    
    def remove(self):
        for child in self.__children:
            child.remove()
        print(f'{self.name}を削除しました')
    
    def add(self, entry: Entry):
        self.__children.append(entry)


if __name__ == '__main__':
    ## 構造
    # dir2 (600)
    # ├── file3 (300)
    # └── dir1 (300)
    #     ├── file1 (100)
    #     └── file2 (200)

    dir1 = Directory('dir1')
    dir2 = Directory('dir2')
    file1 = File('file1', 100)
    file2 = File('file2', 200)
    file3 = File('file3', 300)
    dir1.add(file1)
    dir1.add(file2)
    dir2.add(file3)
    dir2.add(dir1)
    print(dir2.get_size())
    dir2.remove()
    

