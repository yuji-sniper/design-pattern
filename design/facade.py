# Facade

'''
- メリット
    - その他クラスの構成要素を隠蔽することができる

- 使い所
    - 複雑なサブシステムの一部の機能を使用する場合
        - クライアントが内部構造を知らなくても
          シンプルなAPIで機能を利用できる。
    - 複数のクラスの処理を読み出す一連のコードが
      色々な箇所に書かれている場合
'''

class Product:
    def get(self, name: str) -> str:
        return f'{name}を取得しました'

class Payment:
    def make(self, name: str) -> str:
        return f'{name}の支払いを完了しました'

class Invoice:
    def create(self, name: str) -> str:
        return f'{name}の請求書を作成しました'


class Order:
    def place(self, name: str):
        product = Product()
        payment = Payment()
        invoice = Invoice()

        print(product.get(name))
        print(payment.make(name))
        print(invoice.create(name))


if __name__ == '__main__':
    order = Order()
    order.place('apple')
