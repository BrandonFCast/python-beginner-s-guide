###
# pedirle datos al usuairo por consola usando input()
###

# input() retorna el valor en String de lo que haya escrito el usuario
print("dime tu nombre:")
nombre = input()
print(f"Hola {nombre}") #saluda al usuario por su nombre


# input() tambien tiene un parametro opcional para pedir el input con un texto
# este codigo funciona igual que el trozo anterior solo que pedirá
# el apodo en la misma linea, para obtener el mismo resultado podemos
# agregar \n al final de la pregunta
apodo = input("¿Cúal es tu apodo? ")
print(f"Hola {apodo}")


# todo lo que venga de input() es string por lo que si queremos trabajar
# con números tendremos que cambiarlos de tipo
num1 = input("dime el primer numero de la suma: ")
num2 = input("dime el segundo numero de la suma: ")
suma = int(num1) + int(num2)
print(f"la suma es {suma}")