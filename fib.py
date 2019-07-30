"""
>>> fib(7)
13
>>> fib(10)
55
>>> fib(12)
144
>>> fib(6)
8
>>> fib(1)
1
>>> fib(18)
2584

#design comments:
1.The simplest instance is when n=1, and the term in sequence is also one
2.The general problem is any n should give corresponding term in the sequence, just like it did for n=1
3.The smaller instance is not needed when n=0, the sequence starts from n=1
4.Will solve the base case directly which will b n=1
5.The smaller instance for the problem will follow recursion to reach the base case
"""

from math import *
# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print("Can't find logic.py; if this happens in the CS teaching lab, tell your instructor")
    print("   If you are using a different computer, add logic.py to your project")
    print("   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)")
    sys.exit(1)

def fib(n: int):
    precondition(n>0 and type(1)==type(n)) #nth position is an integer position(not float etc) and there is no position 0 for this code
    if n==1 or n==2: #providing the if statements(base cases)
        return 1 #returns 1 for n=2 or n=1
    else:
        return fib(n-1)+fib(n-2) #else returns the nth number in sequence using recursion
    
    
    #
    
    
    
    #the answer must be equal to or more than 1 and must be a positive integer
    
    return answer

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"))
    else:
        print("Rats!")

if __name__ == "__main__": _test()
