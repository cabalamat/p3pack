# top.py = top-directory code

from mymodule import moda

if __name__=='__main__':
    print("=== top.py ===")
    r = moda.add3(6, 2, 9)
    print("result is %r" % (r,))

#end