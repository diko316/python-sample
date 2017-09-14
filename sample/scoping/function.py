

name = "Sample"


def run1():
    """ Test if name exist in this scope """
    name = "another name"
    print "scoping test"
    print name

    
def run2():
    """ Test if name exist in this scope """
    print "scoping test 'name'"
    print name