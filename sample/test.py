"""Test module exposing run() and show() methods. """

from sample.oop import TestClass


name = "Sample"

def run():
    """Just showing "test" string """
    print "test"


def show():
    """Just showing "show!" string """
    print "show!"



# scoping


def scoping():
    """ Test if name exist in this scope """
    name = "another name"
    print "scoping test"
    print name

    
def scoping_next():
    """ Test if name exist in this scope """
    print "scoping test 'name'"
    print name



# class
def test_class():
    """ Test python class """
    mytest = TestClass()
    mytest.log()
