import unittest
import re

class TestAddress(unittest.TestCase):
    test_addresses = ['171.68.120.214', '40.31.1.144', '10.14.14.14', '40.31.1.50', '40.31.1.60', '10.14.14.15', '40.31.1.77', '40.31.1.1', '171.68.118.0', '40.31.1.1', '171.68.120.0', '40.31.1.1', '171.68.118.143', '40.31.1.144', '171.68.118.143', '171.68.118.143', '171.68.118.143', '171.68.120.214']
    
    def test_is_address(self):
        add_ex = re.compile('\S+.\S+.\S+.\S')
        self.assertFalse(add_ex.match('sheep'))
        for address in self.test_addresses:
            self.assertTrue(add_ex.match(address))

if __name__ == '__main__':
    unittest.main()

