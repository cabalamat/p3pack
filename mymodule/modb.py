# modb.py = test moda.py

import moda

def callAdd3(x):
    return moda.add3(x, x, x)

def testModA():
    print("----- testing moda.py -----")
    result = moda.add3(100, 20, 4)
    print("Result=%r, should be 124" % (result,))

if __name__=='__main__':
    testModA()

#end
