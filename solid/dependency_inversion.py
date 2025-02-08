# 依存性逆転の法則

from abc import ABCMeta, abstractmethod


class User:
    pass


class IUserService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def find(self, id: str) -> User:
        pass


class UserController:
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    def create(self, user: User) -> User:
        return self.user_service.create(user)

    def find(self, id: str) -> User:
        return self.user_service.find(id)


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def find(self, id: str) -> User:
        pass


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
    
    def create(self, user: User) -> User:
        return self.user_repository.create(user)
        return user

    def find(self, id: str) -> User:
        return self.user_repository.find(id)
        return User()


class UserRepository(IUserRepository):
    def create(self, user: User) -> User:
        print('ユーザーを作成しました')
        return user

    def find(self, id: str) -> User:
        print(f"ID: {id} のユーザーを取得しました")
        return User()


class MockUserRepository(IUserRepository):
    def create(self, user: User) -> User:
        print('[Mock] ユーザーを作成しました')
        return user

    def find(self, id: str) -> User:
        print(f"[Mock] ID: {id} のユーザーを取得しました")
        return User()


if __name__ == '__main__':
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    user_controller = UserController(user_service)
    user_controller.create(User())
    user_controller.find('1')
    
    mock_user_repository = MockUserRepository()
    user_service = UserService(mock_user_repository)
    user_controller = UserController(user_service)
    user_controller.create(User())
    user_controller.find('1')
