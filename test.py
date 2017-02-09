import os
def print_directory_contents(sPath):
    for i in os.listdir(sPath):
        ipath = os.path.join(sPath,i)
        if os.path.isdir(ipath):
            print_directory_contents(ipath)
        else:
            print(ipath)

# print_directory_contents('D:\W\python\learn')

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)


#
# def multipliers():
#   return [lambda x ,i = i : i * x for i in range(4)]
#
# print([m(3) for m in multipliers()])
#
#
# def div1(x,y):
#     print("%s/%s = %s" % (x, y, x/y))
#
# def div2(x,y):
#     print ("%s//%s = %s" % (x, y, x//y))
#
# div1(5,2)
# div1(5.,2)
# div2(5,2)
# div2(5.,2.)

