from player import Player


class You(Player):
    def confirm_call(self):
        self.show_current_score()
        command = input("カードを引きますか？　引く場合はYを、引かない場合はNを入力してください\n").lower()
        return command == "y"

    def score_showable(self, second_deal=False):
        return True

    def turn_message(self):
        return f"\n{self.name}の手番です。"
