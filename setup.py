""" Just trying to run sample.test.run()
"""

from sample import test

print test.name
print "1. Test Run"
test.run()

print "2. Scoping"
test.scoping()
print "-- next"
test.scoping_next()


print "3. Class"
test.test_class();