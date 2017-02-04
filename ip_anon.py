import re
import ipaddress
from netaddr import *
import pprint

def list_iter(a_list):
    '''
    Generator function that takes a list as input.
    Checks if items in list can be split into 4 . separated octets and if mask is /24 or 0.0.0.0 and yields the item.
    Expand this using binary conversion to evaluate for IP MASK pairings.
    '''
    for item in a_list:
       if (len(item.split('.')) == 4) and '0.0.0.0' not in item:
           yield item

class IPAnon:
    def __init__(self, config):
        with open(config) as f:
            config_lines = f.readlines()
        self.config_lines = config_lines
        self.enum_config_lines = list(enumerate(config_lines))

    def ip_guess(self):
        ip_config_line = []
        linenum_ips = []
        for (num, line) in self.enum_config_lines:
            splitenumline = line.split()
            ip_or_mask = []
            for word in splitenumline:
                if len(word.split('.')) == 4:
                    print word
                    ip_or_mask.append(word)
                    ip_config_line.append((num,line))
            if ip_or_mask:
                linenum_ips.append((num, ip_or_mask))
        self.ip_config_line = ip_config_line
        self.linenum_ips = linenum_ips

    def ip_address_list(self):
        return


def main():
    #testwords = ['1.10.100.101', 'ladybirds', 'hello.word']
    with open('sample_conf.txt') as f:
        f_lines = f.readlines()
        f_split_lines = [i.split() for i in f_lines]

    #print f_split_lines
    all_ips = []
    for i in f_split_lines:
        for j in list_iter(i):
            all_ips.append(j)
    print('{} \n IPs are: {}'.format(80 * '#', all_ips))

    test_anon_class = IPAnon('sample_conf.txt')
    #print test_anon_class.config_lines
    test_anon_class.ip_guess()
    #print test_anon_class.possible_ips
    test_anon_class.ip_address_list()
    print test_anon_class.ip_config_line
    print 80 * '#'
    print test_anon_class.linenum_ips

if __name__ == '__main__':
    main()
