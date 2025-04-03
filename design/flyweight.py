# Flyweight pattern

'''
- メリット
    - 生成されるインスタンス数を減らすことができる
    - メモリ使用量を削減できる
- デメリット
    - コードが複雑になる
    - 共有されているオブジェクトの変更により、
        想定外のバグを生む可能性がある
- 使いどころ
    - 同一のオブジェクトを大量に使用する必要がある場合
    - インスタンス生成によるメモリ使用量を削減したい場合
    - 例）
        - 文字のスタンプを大量に表示するアプリケーション
'''

class Stamp:
    def __init__(self, char: str):
        self.__char = char
    
    def print_char(self):
        print(self.__char)


class StampFactory:
    def __init__(self):
        self.__pool = {}
    
    def get_stamp(self, char: str) -> Stamp:
        pool = self.get_pool()
        if char not in pool:
            self.__pool[char] = Stamp(char)
        return self.__pool[char]

    def get_pool(self):
        return self.__pool


if __name__ == '__main__':
    factory = StampFactory()
    
    stamp1 = factory.get_stamp('し')
    stamp2 = factory.get_stamp('ん')
    stamp3 = factory.get_stamp('ぶ')
    stamp4 = factory.get_stamp('ん')
    stamp5 = factory.get_stamp('し')
    
    stamp1.print_char()
    stamp2.print_char()
    stamp3.print_char()
    stamp4.print_char()
    stamp5.print_char()
    
    print(factory.get_pool())
