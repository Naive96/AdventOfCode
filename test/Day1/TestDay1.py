import unittest
from src.Day1 import part1
from src.Day1 import part2


class TestDay1(unittest.TestCase):

    def test_part1(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        result = part1.execute(numbers)
        self.assertEqual(result, 514579)

    def test_part2(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        result = part2.execute(numbers)
        self.assertEqual(result, 241861950)
