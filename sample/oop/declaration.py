""" Class declaration """

class Base(object):
    """ Example Base Class """

    def __init__(self):
        print "initialized Base Class"

    @classmethod
    def log(cls):
        """ Log you know hihihii """
        print "log Base Class"


class SubClass(Base):
    """ Example Sub Class """


    def __init__(self):
        Base.__init__(self)
        print "initialized Sub Class"



    @classmethod
    def log(cls):
        """ Log you know hihihii from sub class """
        print "before Base log()"
        super(SubClass, cls).log()
        print "log Sub Class"
