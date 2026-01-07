x=float(input("What is x? "))
y=float(input("What is y? "))
z=round(x+y,2)
print("x + y =", z)
# calculator.py
#if a need a int number, only change int to float

print(f"this is = {z:,}")
# this will add comma as thousand separator

# pedir un numero e imprimir su cuadrado
def main():
    x= int(input("Cual es el numero? "))
    print("El cuadrado es, ", subir(x))
def subir(n):
    return n**2
main()
