import random


class Card:

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    def mark_num(self):
        if self.num == 1:
            return "A"
        elif self.num == 11:
            return "J"
        elif self.num == 12:
            return "Q"
        elif self.num == 13:
            return "K"
        else:
            return str(self.num)

    def mark(self):
        return f"{self.suit}の{self.mark_num()}"

    def score(self):
        return self.num if self.num <= 10 else 10

    @classmethod
    def shuffle(cls):
        suits = ["スペード", "ハート", "ダイヤ", "クラブ"]
        cards = [cls(suit, num) for suit in suits for num in range(1, 13)]
        random.shuffle(cards)
        return cards
