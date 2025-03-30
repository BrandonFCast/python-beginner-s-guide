##
#* en python se usa la funcion print() para mostrar un mensaje en consola
##

# el parametro que tiene es un string que es el mensaje a mostrar
print("Hola Mundo") # imprime el mensaje "Hola Mundo" en la consola

# aqui se estan pasando dos strings como argumentos a la funcion print()
print("hola", "mundo") # imprime el mensaje "hola mundo" en la consola

# por defecto al pasar mas de un parametro se separan con un espacio pero eso se puede cambiar
# usando el parametro nombrado sep que especifica el separador entre los argumentos
print("Hola", "Mundo", sep="-") # imprime el mensaje "Hola-Mundo" en la consola
# los parametros nombrados se pueden usar en cualquier orden

# parametro end que especifica el final de la cadena
# cuando un print termina se agrega un salto de linea por defecto al final del mensaje
# pero se puede cambiar usando el parametro end, por ejemplo
# si queremos que no se haga un salto de linea al final del mensaje y en su lugar se imprima un espacio
print("Hola", end=" ") # imprime el mensaje "Hola" y no hace un salto de linea
print("Mundo") # imprime el mensaje "Mundo" en la misma linea
# la salida final de estas dos lineas es "Hola Mundo" en la misma linea