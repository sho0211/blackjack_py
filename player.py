from abc import abstractmethod


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.pop()
        self.hand.append(card)
        return card

    def score(self):
        total = sum([card.score() for card in self.hand])
        if total > 21:
            total = -1
        return total

    def deal(self, deck):
        first = self.draw(deck)
        self.show_card(first)
        second = self.draw(deck)
        self.show_card(second, second_deal=True)

    def show_card(self, card, second_deal=False):
        if(self.score_showable(second_deal)):
            print(f"{self.name}の引いたカードは{card.mark()}です。")
        else:
            print(f"{self.name}の引いたカードはわかりません。")

    def check_bust(self):
        if self.score() == -1:
            print("バースト！")
            return True
        return False

    def show_current_score(self):
        print(f"{self.name}の現在の得点は{self.score()}です。")

    def show_total_score(self):
        s = self.score()
        if s == -1:
            print(f"{self.name}はバーストしました。")
        else:
            print(f"{self.name}の得点は{self.score()}です。")

    def turn(self, deck):
        print(self.turn_message())
        while not self.check_bust() and self.confirm_call():
            card = self.draw(deck)
            self.show_card(card)

    @abstractmethod
    def confirm_call(self):
        pass

    @abstractmethod
    def score_showable(self, second_deal=False):
        pass

    @abstractmethod
    def turn_message(self):
        pass
