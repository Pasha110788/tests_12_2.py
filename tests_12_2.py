import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
