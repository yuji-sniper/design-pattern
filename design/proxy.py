# Proxy pattern

'''
- メリット
    - オブジェクトへのアクセスが間接的になる
    - 目的のオブジェクトがまだ存在しない場合でも
      開発を進めることができる
    - 容易に新規プロキシの追加が可能
- 使いどころ
    - リクエストの前後に処理を追加したい場合
        - 例）
            - リクエストのキャッシュ
            - リクエストのログ
            - リクエストのセキュリティ
'''

from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, user_id: str):
        pass


class RealServer(Server):
    def handle(self, user_id: str):
        print(f"{user_id}のリクエストを処理")


class Proxy(Server):
    def __init__(self, server: Server):
        self.__server = server
    
    def _authorize(self, user_id: str) -> bool:
        authorized_user_ids = ["user1", "user2", "user3"]
        
        if not user_id in authorized_user_ids:
            raise Exception(f"{user_id}は認証されていません")
    
    def handle(self, user_id: str):
        self._authorize(user_id)
        self.__server.handle(user_id)


if __name__ == "__main__":
    server = RealServer()
    proxy = Proxy(server)
    
    proxy.handle("user4")
