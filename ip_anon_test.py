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
    test_ips = ['171.68.120.214', '40.31.1.144', '10.14.14.14', '40.31.1.50', '40.31.1.60', '10.14.14.15', '40.31.1.77', '40.31.1.1', '171.68.118.0', '40.31.1.1', '171.68.120.0', '40.31.1.1', '171.68.118.143', '40.31.1.144', '171.68.118.143', '171.68.118.143', '171.68.118.143', '171.68.120.214']
    def setUp(self):
        self.ip_anon = IPAnon('sample_conf.txt')

    def test__init__pass(self):
        self.assertTrue(True, IPAnon('sample_conf.txt'))
        #self.assertTrue(self.ip_anon, 'sample_conf.txt')

    def test_ip_guess(self):
        t = IPAnon('sample_conf.txt')
        #print t.config_lines
        t.ip_guess()
        t_ips = t.possible_ips
        #print t_ips
        self.assertEqual(TestIPAnon.test_ips, t_ips)

if __name__ == '__main__':
    unittest.main()


