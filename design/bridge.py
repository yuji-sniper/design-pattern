# Bridge pattern

'''
- メリット
    - 機能の追加や変更が容易
    - プログラム実行時に実装を切り替えることができる
    - 機能や実装のバリエーションが豊富な場合、
        最終的に作成するクラスの数が増えすぎることを防ぐ

- 使いどころ
    - 機能と実装の組み合わせが多い場合
        - 継承のみで実現する場合、組み合わせ数分のクラスを
            作成する必要がある
        - 例えば、機能が3つ、実装が5つある場合、
            3 * 5 = 15のクラスが必要
        - Bridgeパターンを使うと、機能と実装の組み合わせ数分の
            クラスを作成するだけで済む
'''

from abc import ABCMeta, abstractmethod


class MessageApp(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass


class Email(MessageApp):
    def send(self):
        print('Emailメッセージを送信')

class LINE(MessageApp):
    def send(self):
        print('LINEメッセージを送信')

class Facebook(MessageApp):
    def send(self):
        print('Facebookメッセージを送信')


class OS(metaclass=ABCMeta):
    def __init__(self):
        self._app = None
    
    def set_app(self, app: MessageApp):
        self._app = app
    
    @abstractmethod
    def send_message(self):
        pass


class IOS(OS):
    def send_message(self):
        print('iOSから', end='')
        if self._app:
            self._app.send()
        else:
            raise Exception('アプリが設定されていません')

class Android(OS):
    def send_message(self):
        print('Androidから', end='')
        if self._app:
            self._app.send()
        else:
            raise Exception('アプリが設定されていません')


if __name__ == '__main__':
    ios = IOS()
    android = Android()

    ios.set_app(Email())
    ios.send_message()

    android.set_app(LINE())
    android.send_message()
