from card import *
from dealer import *
from you import *


class Blackjack:
    def __init__(self):
        self.deck = Card.shuffle()
        self.players = (You("あなた"), Dealer("ディーラー"))

    def deal(self):
        for p in self.players:
            p.deal(self.deck)

    def start(self):
        for p in self.players:
            p.turn(self.deck)

    def judge(self):
        for p in self.players:
            p.show_total_score()
        print(f"勝者は{self.winner().name}です。")

    def winner(self):
        return max(self.players, key=lambda p: p.score())


game = Blackjack()
game.deal()
game.start()
game.judge()
print("ブラックジャック終了：また遊んでね")
