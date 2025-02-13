# Adapter

'''
- 使いどころ
  - 既存のクラスを使用したいが、
    そのインターフェースが利用したい側のコードと
    互換性がない場合
    - 過去に十分テストされて実績のあるクラスに
      手を加えず再利用したい場合

委譲の利用が推奨される！！！
'''

from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


class NewLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            # ボディ
            {
                'name': 'Alice',
                'age': '20'
            },
            {
                'name': 'Bob',
                'age': '21'
            }
        ]


class JsonToCsvAdapter(Target):
    def __init__(self, adaptee: NewLibrary):
        self.adaptee = adaptee
    
    def get_csv_data(self) -> str:
        json_data = self.adaptee.get_json_data()
        
        header = ','.join(json_data[0].keys())
        body = '\n'.join([','.join(data.values()) for data in json_data])
        
        return f'{header}\n{body}'


if __name__ == '__main__':
    adaptee = NewLibrary()
    print("=== Adapteeが提供するデータ ===")
    print(adaptee.get_json_data())
    
    print("")
    
    adapter = JsonToCsvAdapter(adaptee)
    print("=== Adapterが変換したデータ ===")
    print(adapter.get_csv_data())
