from player import Player


class Dealer(Player):
    def confirm_call(self):
        return self.score() < 17

    def score_showable(self, second_deal=False):
        return not second_deal

    def turn_message(self):
        return f"\n{self.name}の2枚目のカードは{self.hand[1].mark()}でした。\n"
