import unittest

from HCA import Caesar as c


class TestCeasar(unittest.TestCase):
    def test_list_int(self):
        """
        Test Ceasar
        """
        data = "Pack my box with five dozen liquor jugs."
        result = c.encrypt(data)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
