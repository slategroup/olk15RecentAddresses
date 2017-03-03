from nose.tools import *
from RecentAddressesParser.parser import Parser

def setup():
    print "Setup"

def teardown():
    print "Teardown"

def test_basic_func():
    parser = Parser('sample_data/328B48E0-D455-45E3-868A-9506B8004644.olk15RecentAddresses')
    parser.go()
    print "I RAN!"