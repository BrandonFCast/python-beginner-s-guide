##
# Condicionales if, else y elif
## 

# aqui esta el tipico condicional if - else
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# aqui se puede ver el uso de elif para evaluar más de una condición
# tambien aprendemos una funcion nueva llamada len() a la que si le 
# pasamos una cadena de texto nos retorna el numero de caracteres que tiene
nombre = input("dime tu nombre")
if len(nombre) < 5:
    print("Tu nombre es corto")
elif len(nombre) < 8:
    print("Tu nombre es mediano") 
else: # este else es opcional
    print("Tu nombre es largo")