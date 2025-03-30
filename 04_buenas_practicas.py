##
#* buenas practicas para tener en cuenta en python
##

# la forma recomendada de nombrar variables en python es usando snake_case
# lo que significa usar letras minusculas y separar las palabras con guiones bajos
#? por ejemplo:
esta_es_una_variable = 'bien' # snake_case
variable = 'bien' # snake_case

EstaEsUnaVariable = 'mal' # PascalCase #! no recomendado
EstaEsUnaVariable = 'mal' # camelCase #! no recomendado

# no se deben de declarar variables con nombres reservados de python
#? por ejemplo: 
#? no se pueden crear variables llamdas: print, input, if, else, for, while, etc.
#? porque python usa esas palabras para sus funciones y estructuras de control

#* en la programacion existen las constantes las cuales son
#* lo mismo que una variable pero que no cambia su valor
#? por ejemplo:
#? el valor de pi es un valor que no debe cambiar por lo que debe estar en una constante
# en python no hay forma de declarar constantes y evitar que sean cambiadas
# por lo que se recomienda usar mayusculas para indicar que es una constante
# y que al verla saber que no debe ser cambiada
#? por ejemplo:
MI_CONSTANTE = 3.1416 # constante
PI = 3.1416 # constante