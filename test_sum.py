import unittest

from sum import multiply, subofnum, sumofnum

class sumNum(unittest.TestCase):
    def test_sum(self):
        a= 3
        b=4
        response = sumofnum(a,b)
        self.assertEqual(response, a+b)
    
    def test_sub(self):
        a= 3
        b=4
        response = subofnum(a,b)
        self.assertEqual(response, a-b)
    
    def test_sum(self):
        a= 3
        b=4
        response = multiply(a,b)
        self.assertEqual(response, a*b)

if __name__ == '__main__':
    unittest.main()
