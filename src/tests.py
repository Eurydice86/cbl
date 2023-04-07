'''unit tests'''

import unittest
import fight


class TestElo(unittest.TestCase):
    '''unit testing class'''
    def test_elo_calcs(self):
        '''testing the elo calculations'''
        self.assertAlmostEqual(fight.calculate_new_winner_elo(1000,2000), 1039.9, places = 1)
        self.assertAlmostEqual(fight.calculate_new_loser_elo(1000,2000), 1960.1, places = 1)

        self.assertAlmostEqual(fight.calculate_new_winner_elo(2000,2000), 2020, places = 1)
        self.assertAlmostEqual(fight.calculate_new_loser_elo(2000,2000), 1980, places = 1)

        self.assertAlmostEqual(fight.calculate_new_winner_elo(0,2000), 40, places = 1)
        self.assertAlmostEqual(fight.calculate_new_loser_elo(0,2000), 1960, places = 1)


if __name__ == "__main__":
    unittest.main()
