import unittest

from main import ijones


class SuccessfulWaysTest(unittest.TestCase):
    def test_for_one_row(self):
        corridor = [["a", "b", "c", "d", "e", "f", "a", "g", "h", "i"]]
        number_of_successful_ways = ijones(corridor, 10, 1)
        self.assertEqual(2, number_of_successful_ways)

    def test_for_the_same_letters_on_tiles(self):
        corridor = [["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"]]
        number_of_successful_ways = ijones(corridor, 7, 6)
        self.assertEqual(201684, number_of_successful_ways)

    def test_for_square_matrix(self):
        corridor = [["a", "a", "a"], ["c", "a", "b"], ["d", "e", "f"]]
        number_of_successful_ways = ijones(corridor, 3, 3)
        self.assertEqual(5, number_of_successful_ways)


if __name__ == '__main__':
    unittest.main()
