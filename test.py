import unittest
import re

class TestAddress(unittest.TestCase):
    
    def test_is_address(self):
        add_ex = re.compile('\S+.\S+.\S+.\S')
        self.assertFalse(add_ex.match('sheep'))
        self.assertTrue(add_ex.match('100.1.1.1'))

if __name__ == '__main__':
    unittest.main()

