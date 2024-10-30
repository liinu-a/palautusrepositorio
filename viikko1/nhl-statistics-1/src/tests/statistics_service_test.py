import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_players_are_correct(self):
        self.assertEqual(str(self.stats._players[0]), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(str(self.stats._players[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(str(self.stats._players[2]), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(str(self.stats._players[3]), "Yzerman DET 42 + 56 = 98")
        self.assertEqual(str(self.stats._players[4]), "Gretzky EDM 35 + 89 = 124")

    def test_search_found(self):
        self.assertEqual(self.stats.search("Semenko"), self.stats._players[0])

    def test_search_not_found(self):
        self.assertEqual(self.stats.search("A"), None)

    def test_players_of_team(self):
        self.assertEqual(self.stats.team("PIT"), [self.stats._players[1]])

    def test_top_3_players(self):
        top3 = [self.stats._players[4], self.stats._players[1], self.stats._players[3]]
        self.assertEqual(self.stats.top(2), top3)
        