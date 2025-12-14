# Ejemplo: funciones y listas
def saludar(nombre):
    return f"Hola, {nombre}!"

nombres = ["Ana", "Luis", "María"]
for n in nombres:
    print(saludar(n))

# Suma de los pares en una lista
nums = [1,2,3,4,5,6]
suma_pares = sum(x for x in nums if x % 2 == 0)
print(suma_pares)

#Hello world
print("Hola mundo")
  