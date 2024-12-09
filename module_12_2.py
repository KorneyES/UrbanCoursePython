from runner import Runner
from runner import Tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            finishers = cls.all_results[key]
            result_str = f"{key}: " + ", ".join(str(finishers[place]) for place in sorted(finishers.keys()))
            print(result_str)

    def test_usain_vs_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    def test_andrey_vs_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

    def test_usain_and_andrey_vs_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == self.nik)

if __name__ == '__main__':
    unittest.main()