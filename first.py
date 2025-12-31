
"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird. 
""" 
if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")

#Starting point of program
           
print("Hello, World!")
# I can use: code "first.py" to run this file in terminal
# and i can use: python "first.py"  to run this file in terminal
#print(), input(), are functions used to output and input data in python

#Ask for user their name 
name=input("Enter your name: ")
#Say hello to the user
print("Hello " + name)
print("Hello", name)
"""
C++ code for the same program
cout<< "Enter ur name" << endl;
cin>>name;

"""


