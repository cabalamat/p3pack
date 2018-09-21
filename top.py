# top.py = top-directory code

from mymodule import moda, modb

if __name__=='__main__':
    print("=== top.py ===")
    r = moda.add3(6, 2, 9)
    print("result is %r" % (r,))
    r2 = modb.callAdd3(7)
    print("r2 is %r" % (r2,))

#end