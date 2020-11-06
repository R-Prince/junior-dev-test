import unittest
from datetime import date
from main import User


class TestClass (unittest.TestCase):

    def test_return_correct_age(self):
        today = date.today()

        # Tests
        test1 = User("test1", date(1986, 1, 1))
        test2 = User("test2", date(1988, today.month, today.day))
        test3 = User("test3", date(1990, 12, 30))

        # Action to determine age
        result1 = test1.age()
        result2 = test2.age()
        result3 = test3.age()

        # Assert - Results function should return
        self.assertEqual(result1, 34)
        self.assertEqual(result2, 32)
        self.assertEqual(result3, 29)

    def test_return_correct_next_birthday(self):
        today = date.today()

        # Tests
        test1 = User("test1", date(1986, 1, 1))
        test2 = User("test2", date(1988, today.month, today.day))
        test3 = User("test3", date(1990, 12, 30))

        # Action to determine next birthday
        result1 = test1.next_birthday()
        result2 = test2.next_birthday()
        result3 = test3.next_birthday()

        # Assert - Results function should return
        self.assertEqual(result1, date(2021, 1, 1))
        self.assertEqual(result2, date(2021, 11, 6))
        self.assertEqual(result3, date(2020, 12, 30))
