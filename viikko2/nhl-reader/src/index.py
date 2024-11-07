import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = sorted(
            filter(lambda player: (player.nationality == 'FIN'), players),
        key=lambda player: player.points, reverse=True)
    
    print("Players from FIN:\n")

    for player in fin_players:
        print(player)


if __name__ == "__main__":
    main()
