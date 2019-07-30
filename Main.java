package basic;

public class Main {
	
	public static void main(String[] args) {
		// TODO: You should call the functions you create from this function in order to test them.
		// You can check that your Eclipse setup is correct by running this file - you should see
		// the below printout in the Console window.  After that, you may remove it.
		System.out.println("Welcome to CS 106!  Enjoy Lab 0!");
		//checking if the functions work correctly
		System.out.println(exp(2,3));
		System.out.println(exp(5,2));
		System.out.println(exp(10,0));
		System.out.println(exp(9,5));
		System.out.println(exp(0,1));
		
		System.out.println(gcd(6,8));
		System.out.println(gcd(0,5));
		System.out.println(gcd(5,0));
		System.out.println(gcd(144,48));
		
		System.out.println(isPrime(11));
		System.out.println(isPrime(1198));
		System.out.println(isPrime(1));
		System.out.println(isPrime(4));
		System.out.println(isPrime(17));
		
		System.out.println(round(33.4));
		System.out.println(round(0.4));
		System.out.println(round(128.5));
		System.out.println(round(66.66));
		
		Prerequisites prereqs = Prerequisites.CS340;
		printPrerequisites(prereqs);
		Prerequisites pr = Prerequisites.CS350;
		printPrerequisites(pr);
		Prerequisites prereq = Prerequisites.CS210;
		printPrerequisites(prereq);

		
	}
	
	// TODO: You should add the functions you create for the lab here and below.
	
	// This function raises a base to the power using a while loop
    public static int exp(int base, int exponent) { //There are two integer variables
    int result= 1; //Initializing the result which is base raised to 0
    while (exponent !=0) { //loop guard is exponent not equal to 1
    	result = result*base; //this changes the previous value of result
    	--exponent;} //this decreases the exponent value by one so there is progress and eventually termination
    return result;
    }
    //this function finds the gcd of two integers using Euclid method
    public static int gcd(int a, int b) { //two variables are any two integers
        if (b == 0) return a; //if b is 0 then a is the gcd
        else return gcd(b, a % b); //recursion takes place and function keeps on finding remainders until the other number is 0
     }
    
    //this function tells if the number is prime or not
    public static Boolean isPrime(int n){  //n is the variable integer
    	if (n <= 1) 
    		return false; //if the number is 1 or less then its not prime. its the base case
        for (int i = 2; i < n; i++) //using a for loop to check
            if (n % i == 0) //keeps on checking for remainders in case there are none meaning its not prime
            	return false; 
        return true; //true if there are remainders and and its not divided by anything else except the number itself
        }
    
   //rounds a double to an integer 
    public static int round(double d) {//the variable should be a double
        if (d > 0) { //if a positive number, check by rounding to next greater positive number
            return (int) (d + 0.5); //adding 0.5 so it gets closest to the integer eg if the decimal point is below 5, it'll max become 0.9 and hence when written as integer, will be rounded correctly
        } else {
            return (int) (d - 0.5); //almost same argument as above but since its negative number, have to subtract 0.5 so it is rounded correctly
        }}
    
    //enum that prints out prereqs for the given 3 courses
    public enum Prerequisites {CS340,CS350,CS356,CS210,CS105}; //defining the enum and writing courses
    public static void printPrerequisites(Prerequisites prerequisites) {
    switch (prerequisites) {
    case CS340: //if we give this course
    	System.out.println("CS105,CS106, and CS231"); //it'll print out these prereqs. Same for the two other courses
    	break;
    case CS350:
    	System.out.println("CS245");
    	break;
    case CS356:
    	System.out.println("CS240");
    	break;
    default: //prints the message if  cs210 or cs105 are input because we haven't defined a case for them
    	System.out.println("I don't know this course.");
    	break;
    } 
    }
 }


