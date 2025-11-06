import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan statisticsservice-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())


    def test_toimiikotestit(self):
        self.assertEqual("Hello World","Hello World")


    def test_search(self):
        pelaaja = self.stats.search("Gretzky")
        print(pelaaja)
        oikea = Player("Gretzky", "EDM", 35, 89)
        self.assertAlmostEqual(print(pelaaja), print(oikea))


    def test_team(self):
        #list_pit = list(Player("Lemieux", "PIT", 45, 54))
        #print(list_pit)
        haku = self.stats.team("PIT")

        print(haku[0])

        self.assertAlmostEqual(haku[0].name, "Lemieux")


    def test_top(self):
        haku = self.stats.top(2)

        self.assertAlmostEqual(haku[0].name, "Gretzky")
        self.assertAlmostEqual(haku[1].name, "Lemieux")
