# Factory Method

from abc import ABCMeta, abstractmethod


class CreditCard(metaclass=ABCMeta):
    def __init__(self, owner: str):
        self.__owner = owner
    
    @property
    def owner(self) -> str:
        return self.__owner
    
    @abstractmethod
    def get_card_type(self) -> str:
        pass
    
    @abstractmethod
    def get_annual_charge(self) -> int:
        pass


class Platinum(CreditCard):
    def get_card_type(self) -> str:
        return "Platinum"
    
    def get_annual_charge(self) -> int:
        return 30000

class Gold(CreditCard):
    def get_card_type(self) -> str:
        return "Gold"
    
    def get_annual_charge(self) -> int:
        return 10000


class CreditCardFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_card(self, owner: str) -> CreditCard:
        pass

    @abstractmethod
    def register_card(self, card: CreditCard):
        pass
    
    def create(self, owner: str) -> CreditCard:
        card = self.create_card(owner)
        self.register_card(card)
        return card


credit_card_database: list[CreditCard] = []

class PlatinumFactory(CreditCardFactory):
    def create_card(self, owner: str) -> CreditCard:
        return Platinum(owner)
    
    def register_card(self, card: CreditCard):
        credit_card_database.append(card)

class GoldFactory(CreditCardFactory):
    def create_card(self, owner: str) -> CreditCard:
        return Gold(owner)
    
    def register_card(self, card: CreditCard):
        credit_card_database.append(card)


if __name__ == "__main__":
    platinum_factory = PlatinumFactory()
    gold_factory = GoldFactory()

    platinum_card = platinum_factory.create("Tom")
    gold_card = gold_factory.create("Jerry")

    print(platinum_card.owner, platinum_card.get_card_type(), platinum_card.get_annual_charge())
    print(gold_card.owner, gold_card.get_card_type(), gold_card.get_annual_charge())

    for card in credit_card_database:
        print(card.owner, card.get_card_type(), card.get_annual_charge())
