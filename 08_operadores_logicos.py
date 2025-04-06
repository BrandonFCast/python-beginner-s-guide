##
#* operadores logicos como and, or y not
##

# and: retorna true si ambas condiciones son true
# or: retorna true si una de las condiciones es true
# not: retorna el opuesto de la condición

#* en otros lenguajes se usan otros simbolos para los operadores logicos
#? por ejemplo:
#? en java, javascript, c#, c++ se usan && para and, || para or y ! para not


#* los operadores logicos actuan con expresiones booleanas

#* and: retorna true si ambas condiciones son true
#? por ejemplo:
#? si tenemos una variable edad y queremos saber si es mayor de 18 y menor de 60
#? podemos usar el operador and para evaluar ambas condiciones
edad = int(input("Dime tu edad: "))
if edad > 18 and edad < 60:
    print("Eres mayor de 18 y menor de 60")

#* not: retorna el opuesto de la condición
#? por ejemplo:
#? si tenemos una variable edad y queremos saber si es menor de 18
#? podemos usar el operador not para evaluar la condición
if not edad > 18: # aqui se esta diciendo: si edad no es mayor de 18 ejecuta el codigo de abajo
    print("Eres menor de 18")


#* operacion ternario en python
mensaje = "Eres mayor de 18" if edad > 18 else "Eres menor de 18"
print(mensaje)