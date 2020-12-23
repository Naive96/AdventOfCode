import unittest
from src.Day2 import part1
from src.Day2 import part2


class TestDay2(unittest.TestCase):

    def test_part1(self):
        pwds = ['1-3 a: abcde',
                '1-3 b: cdefg',
                '2-9 c: ccccccccc']
        result = part1.execute(pwds)
        self.assertEqual(result, 2)

    def test_part2(self):
        pwds = ['1-3 a: abcde',
                '1-3 b: cdefg',
                '2-9 c: ccccccccc']
        result = part2.execute(pwds)
        self.assertEqual(result, 1)
