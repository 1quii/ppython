"""
#use def to define a function
def greet_user():
    #Ask for user their name 
    name=input("Enter your name: ").strip().title()
    #Say hello to the user
    print("Hello,", name)   

def hello(para="Usuario"):
    print("Hello,", para)
    
hello()
name=input("Enter your name: ").strip().title()
hello(name) 
"""
def hello(to="Everyone"):
    print("Hello,", to)

def main():
    nombre=input("Whats your name? ").strip().title()
    hello(nombre)


main ()