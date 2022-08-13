import unittest
import driver


class TestAlternator(unittest.TestCase):
    def test_alternate_o(self):
        initial_player = 'X'
        changed_player = driver.alternator(initial_player)
        self.assertEqual(changed_player, 'O')

    def test_alternate_x(self):
        initial_player = 'O'
        changed_player = driver.alternator(initial_player)
        self.assertEqual(changed_player, 'X')

    def test_alternate_bad_val(self):
        initial_player = 'Y'
        with self.assertRaises(ValueError):
            driver.alternator(initial_player)


class TestIsNumber(unittest.TestCase):
    def test_number(self):
        number = 1
        b = driver.is_number(number)
        self.assertTrue(b)

    def test_not_number(self):
        number = 'not number'
        b = driver.is_number(number)
        self.assertFalse(b)


if __name__ == '__main__':
    unittest.main()
