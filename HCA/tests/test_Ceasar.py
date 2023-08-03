import unittest

from HCA import Caesar as c


class TestCeasar(unittest.TestCase):

    def test_list_int(self):
        """ Test Ceasar """
        data = "Pack my box with five dozen liquor jugs."
        result = c.encrypt(data, 6)
        self.assertEqual(result, "Vgiq se hud cozn lobk jufkt rowaux pamy.")
        revers = c.decrypt(result, 6)
        self.assertEqual(revers, data)


if __name__ == '__main__':
    unittest.main()
