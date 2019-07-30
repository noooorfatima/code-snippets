"""
Here are some examples of how to test GCD, reduced(), and reduce()

>>> GCD(3, 6)
3
>>> GCD(12, 18)
6

>>> inReducedForm([3, 6])
[1, 2]

>>> test0 = [3, 6]
>>> inReducedForm(test0)
[1, 2]
>>> test0  # this should NOT have been changed by a function
[3, 6]


>>> test1 = [3,6]
>>> reduce(test1)
>>> test1
[1, 2]

>>> test2 = [1,2]
>>> reduce(test2)
>>> test2
[1, 2]

>>> test3 = [3,6]
>>> test4 = test3
>>> inReducedForm(test3)
[1, 2]
>>> test3
[3, 6]
>>> reduce(test3)
>>> test3
[1, 2]
>>> test4
[1, 2]

>>> GCD(6, 30)
6
>>> GCD(0, 50)
50
>>> GCD(0, 0)
0
>>> GCD(5, 5)
5
>>> GCD(8, 64)
8
>>> GCD(9, 6)
3
>>> GCD(-4,-16)
-4
>>> inReducedForm([5, 25])
[1, 5]
>>> inReducedForm([20, 100])
[1, 5]
>>> inReducedForm([7, 42])
[1, 6]
>>> inReducedForm([4, 10])
[2, 5]
>>> inReducedForm([-6, -12])
[1, 2]
>>> inReducedForm([30, 15])
[2, 1]
>>> test1 = [4,8]
>>> inReducedForm(test1)
[1, 2]
>>> test1
[4, 8]
>>> reduce(test1)
>>> test1
[1, 2]
>>> test2 = [3,9]
>>> inReducedForm(test2)
[1, 3]
>>> test2
[3, 9]
>>> reduce(test2)
>>> test2
[1, 3]




"""
# make Python look in the right place for logic.py, or complain if it doesn't
from fractions import gcd
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print ("Can't find logic.py; if this happens in the CS teaching lab, tell your instructor")
    print ("   If you are using a different computer, add logic.py to your project")
    print ("You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py")
    sys.exit(1)

# Hopefully the following will stop any infinite loops without killing anything correct
import resource
resource.setrlimit(resource.RLIMIT_CPU, [3, 5])


def GCD(x,y):
    #precondition:x and y are integers 
    if y==0:
        return x
    else:
        return GCD(y, x%y) #recursion takes place here
    ####################################################################



# A possibly-useful function for assertions:

def isFraction(hopedForFractionInAList):
    return (type(hopedForFractionInAList) == type([1, 2]) and
            isInteger(hopedForFractionInAList[0]) and
            isInteger(hopedForFractionInAList[1]))

def inReducedForm(fractionInAList):
    #precondition the parameter is an array/list containing two elements
    a=fractionInAList[0] #a is defining the first element
    b=fractionInAList[1] #b is the second element
    gcd=GCD(a,b) #finding gcd for the elements in the list
    new=[int((fractionInAList[0])/gcd),int((fractionInAList[1])/gcd)] #defining a new list so that original remains unchanged
    return new
    
        

def reduce(fractionInAList):
    #precondition the parameter is an array/list containing two elements
    gcd=GCD(fractionInAList[0],fractionInAList[1]) #gcd for the list elements
    fractionInAList[0]=int(fractionInAList[0]/gcd) #changing the first element of the list
    fractionInAList[1]=int(fractionInAList[1]/gcd) #changing the second element of the list
    
    
    
    

# User interface for reduce, which should be defined above (as should GCD)
# Do NOT change this, but you can write your own if you like
def reduceUI():
    n = input("Enter numerator ")
    d = input("Enter non-zero denominator (or 0 to stop) ")
    while (d != 0):
        result = inReducedForm([n, d])
        print ("""According to "inReducedForm", that's""", result[0], "/", result[1], "in reduced terms.")

        fractionInList = [n, d]
        reduce(fractionInList)
        print ("""According to "reduce", that's""", fractionInList[0], "/", fractionInList[1], "in reduced terms.")

        n = input("Enter another numerator ")
        d = input("Enter another non-zero denominator (or 0 to stop) ")

    print ("Thanks for playing the fractions game!")

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print ("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": 
    _test()
    reduceUI()

