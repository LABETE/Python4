"""
Test list-of-list based array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                for j in range(N):
                    self.assertEqual(a[i, j], 0)
    
    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N)
            for i in range(N):
                a[i, i] = 1
                print(i, "a")
                print(a[i, i], "b")
            for i in range(N):
                for j in range(N):
                    print(a[i,j], "c")
                    print(i == j, "d")
                    self.assertEqual(a[i, j], i==j)
    
    def _index(self, a, r, c):
        return a[r, c]
    
    def test_key_validity(self):
        a = arr.array(10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1)
        self.assertRaises(KeyError, self._index, a, 1, 10)

if __name__ == "__main__":
    unittest.main()