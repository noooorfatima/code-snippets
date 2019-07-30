"""
>>> is_palindrome("kayak") #it is a palindrome, same word backwords, so true
True
>>> is_palindrome("racecar")
True
>>> is_palindrome("asantaatnasa")
True
>>> is_palindrome("keyboard") #not the same word backwards hence false
False
>>> is_palindrome("pleaselogoff")
False
>>> is_palindrome("helloworld") 
False

#Design comments:
1.Smaller instance of the problem is if the letter in string is same backwards(base case will be just one or no letter)
2.General problem will be same for a more than one letter string(should be same backwards)
3.The smaller instance will not work if directly if letters exceed 1, need recursion then
4.Solve base case of one or zero letter directly
5.Using the base case, we can use recursion to identify if the string is a palindrome
"""

# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print( "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor")
    print( "   If you are using a different computer, add logic.py to your project")
    print( "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)")
    sys.exit(1)

def is_palindrome(letters):
    #precondition: only letters, and all lower case. No non-letters or empty and string
    if len(letters)<=1: #base case of one lettered or empty string
        return True
    else:
        if letters[0]==letters[-1]: #if the first and last letters are same then it starts recursion
            return is_palindrome(letters[1:-1]) #recursion happens as this checks if first and last letters are same by chopping off end letters and eventually reaching the base case

        else:
            return False #returns false if first and last letters are not the same
    


    #postcondition: answer is true if letters is equal to letters[::-1] otherwise false



# User interface for the palindrome function
def palindrome_ui():
    if __name__ == "__main__":
        print ("Type 1 to run your test-suite, press 2 to type in your own tests:")
        answer = input()
        if answer in ['1']:  
            _test()
        else:
            print("Please input a possible palindrome: ")
            trial_text = input()
            letters_only = lower_case_letters(trial_text)
            if is_palindrome(letters_only):
                print("The text '"+letters_only+"' is a palindrome")
            else:
                print("The text '"+letters_only+"' is not a palindrome.")

"""
    make something all lower case letters, e.g.

>>> lower_case_letters('kayak')
'kayak'
>>> lower_case_letters('A man, a plan, a canal: Panama!')
'amanaplanacanalpanama'
"""

def lower_case_letters(text):
    if text == '':
        return ''
    else:
        first = text[0]
        rest  = text[1:len(text)]
        if first in 'abcdefghijklmnopqrstuvwxyz':  # already lower case
            return first + lower_case_letters(rest)
        elif first in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': # upper-case
            # lower(first) turns, for example, "D" into "d"
            from string import lower
            return lower(first) + lower_case_letters(rest)
        else:   # otherwise skip first element, as it's not a letter
            return lower_case_letters(rest)

# mostly copied from  http://docs.python.org/lib/module-doctest.html

def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

# tests may or may not be chosen by the user interface...
if __name__ == "__main__": palindrome_ui()

