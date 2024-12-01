class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def get_score_name(self, score_num):
        match score_num:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"

    def equal_score(self):
        score_num = self.player1_score
        if score_num >= 3:
            self.score = "Deuce"
            return
        self.score = self.get_score_name(score_num) + "-All"

    def winner(self, point_difference):
        if point_difference >= 2:
            self.score = f"Win for {self.player1_name}"
        else:
            self.score = f"Win for {self.player2_name}"

    def score_over_40(self):
        point_difference = self.player1_score - self.player2_score

        match point_difference:
            case 1:
                self.score = f"Advantage {self.player1_name}"
            case -1:
                self.score = f"Advantage {self.player2_name}"
            case _:
                self.winner(point_difference)

    def scores_under_40(self):
        score_name_player1 = self.get_score_name(self.player1_score)
        score_name_player2 = self.get_score_name(self.player2_score)
        self.score = score_name_player1 + "-" + score_name_player2

    def set_score(self):
        if self.player1_score == self.player2_score:
            self.equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            self.score_over_40()
        else:
            self.scores_under_40()

    def get_score(self):
        self.set_score()
        return self.score
