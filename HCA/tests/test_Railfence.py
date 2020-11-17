import unittest

from HCA import Railfence as c

class TestRailfence(unittest.TestCase):
    def test_list_int(self):
        """ Test RailFence
        P   ¤   b   w   ¤   e   z   l   o   u
         a k m ¤ o ¤ i h f v ¤ o e ¤ i u r j g .
          c   y   x   t   i   d   n   q   ¤   s
        """
        data = "Pack my box with five dozen liquor jugs."
        result = c.encrypt(data, 3)
        self.assertEqual(result, "P bw ezlouakm o ihfv oe iurjg.cyxtidnq s")
        revers = c.decrypt(result, 3)
        self.assertEqual(revers, data)

if __name__ == '__main__':
    unittest.main()
