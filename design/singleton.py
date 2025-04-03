# Singleton

'''
メリット：
- インスタンスが1つしか生成されないことを保証する
-　インスタンスが1つだからメモリ効率が良い
- インスタンスが1つだから、インスタンス間のデータの共有が容易

デメリット：
- マルチスレッド環境で競合が発生する可能性がある
- 単体テストが困難

使いどころ：
- プログラム内のクラスで、全てのクライアントが
  使用できるインスタンスを必ず1つだけにしたい場合。
  - ロギング
  - キャッシュ管理
  - データベース接続
  - コンフィグ

今はアンチパターンとされている！！
'''

import datetime


class Logger:
    _instance = None
    
    '''
    - __new__メソッド
      - インスタンス生成時に最初に呼ばれる
      - インスタンスをどう作るかを制御
    - ロジック
      - インスタンスが存在しなければ新しく作成
      - すでに作成されたインスタンスがあればそれを使い回す
    '''
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def output(self, content: str):
        now = datetime.datetime.now()
        print(f'{now}: {content}')


class Test:
    pass


if __name__ == '__main__':
    test1 = Test()
    test2 = Test()
    print("Test: ", test1 == test2)
    
    logger1 = Logger()
    logger2 = Logger()
    print("Logger: ", logger1 == logger2)
    
    logger1.output('logger1のログ')
    logger2.output('logger2のログ')
