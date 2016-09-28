import unittest
from ip_anon import IPAnon

'''
class IPAnon:
    def __init__(self, config):
        with open(config) as f:
            config_lines = f.readlines()
        self.config_lines = config_lines
IOError: [Errno 2] No such file or directory: 'ample_conf.txt'
'''

class TestIPAnon(unittest.TestCase):
    def setUp(self):
        self.ip_anon = IPAnon('sample_conf.txt')

    def test__init__pass(self):
        self.assertTrue(True, IPAnon('sample_conf.txt'))
        #self.assertTrue(self.ip_anon, 'sample_conf.txt')

    def test_ip_guess(self):
        t = IPAnon('sample_conf.txt')
        self.assertTrue(t.ip_guess(), ['100.1.1.1'])
        

if __name__ == '__main__':
    unittest.main()


