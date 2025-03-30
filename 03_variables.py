##
#* para declarar una variable en python
#* basta con escribir el nombre de la variable y asignarle un valor 
##

mi_variable = 10 # declaracion de variable

print("mi_variable es: ", mi_variable) # imprime el valor de la variable
print("mi_variable es de tipo: ", type(mi_variable)) # imprime el tipo de la variable

# reasignacion de valores
mi_variable = 20 # reasignacion de variable
print("mi_variable es: ", mi_variable) # el valor ahora es 20

# el tipo de dato es dinamico lo que hace que se puede cambiar el tipo de la variable
# durante la ejecucion del programa

mi_variable = "Hola mundo" # reasignacion de variable y de tipo de dato
print("mi_variable es: ", mi_variable)
print("mi_variable es de tipo: ", type(mi_variable)) # el tipo de dato ahora es un string


# se pueden asignar más de una variable en la misma linea
# el primer valor se asigna a la primera variable y el segundo valor a la segunda variable
# asi con cualquier cantidad de variables
mi_variable1, mi_variable2 = 10, "hola"
# mi_variable1 es un entero y mi_variable2 es un string
##### ! esto no se recomienda porque puede ser confuso y no es legible pero esta bien saberlo