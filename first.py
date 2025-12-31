

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
print("hello,", end=" ")
print(name)
print("Hello,", name,sep="***")
print(f"Hello, {name}")

"""
#strip() function is used to remove any extra spaces before and after the input
age=int(input("Enter your age: ").strip())

name=name.strip()
#remove whitespaces from str

name= name.capitalize()
#capitalize the first letter of the string

name=name.title()
#capitalize the first letter of each word in the string
"""
#Despues de lo aprendido:
name=input("Enter name ").strip().title()
print("Hello,", name)

#split user name
first, last = name.split(" ")
print("Hello,", first, last)
print("First name:", first)
print("Last name:", last)

