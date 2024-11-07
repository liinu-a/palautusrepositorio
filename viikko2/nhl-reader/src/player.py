import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.points = self.assists + self.goals

    def __str__(self):
        return f'{self.name:20} {self.team:4} {self.goals:2} + {self.assists:2} = {self.points}'
    

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        return [Player(player_dict) for player_dict in self.response]


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nat):
        return sorted(filter(
                lambda player: (player.nationality == nat), self.players
            ), key=lambda player: player.points, reverse=True)
