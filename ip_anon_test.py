import unittest
from ip_anon import IPAnon
import ipaddress

'''
class IPAnon:
    def __init__(self, config):
        with open(config) as f:
            config_lines = f.readlines()
        self.config_lines = config_lines
IOError: [Errno 2] No such file or directory: 'ample_conf.txt'
'''

class TestIPAnon(unittest.TestCase):
    test_ips = ['171.68.120.214', '40.31.1.144', '255.255.255.0', '10.14.14.14', '255.255.255.0', '40.31.1.50', '40.31.1.60', '255.255.255.0', '10.14.14.15', '40.31.1.77', '40.31.1.1', '171.68.118.0', '255.255.255.0', '40.31.1.1', '171.68.120.0', '255.255.255.0', '40.31.1.1', '171.68.118.143', '40.31.1.144', '171.68.118.143', '171.68.118.143', '171.68.118.143', '171.68.120.214']
    test_interface_objects = [IPv4Interface('40.31.1.144/24'), IPv4Interface('10.14.14.14/24'), IPv4Interface('40.31.1.60/24'), IPv4Interface('171.68.118.0/24'), IPv4Interface('171.68.120.0/24')]
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
        self.assertEqual(TestIPAnon.test_ips, t_ips)

    def test_ip_address_list(self):
        t = IPAnon('sample_conf.txt')
        t.ip_guess()
        t.ip_address_list()
        self.assertEqual(test_interface_objects, t.config_interfaces)

if __name__ == '__main__':
    unittest.main()


