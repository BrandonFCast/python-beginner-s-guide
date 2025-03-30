print("tipos de datos basicos en python")

# numeros enteros (int)
print(type(10))
print(type(0))
print(type(-3))
print(type(12983812127845736))

# numeros con decimal (float)
print(type(10.0))
print(type(0.0))
print(type(-3.0))
# en python se puede usar la notacion cientifica y el resultado siempre es flotante
print(type(3e10))#? esto es 3x10^2

# numeros complejos (complex)
print(type(10+5j))

# cadenas de texto (str)
print(type("Hola mundo"))
print(type('Hola mundo'))
print(type("""
           Cadena de texto multilinea
           """))
print(type('''
           Cadena de texto multilinea
           '''))
print(type("123"))

# boleanos (bool)
print(type(True))
print(type(False))
print(type(10 > 5))

# sin valor (none)
print(type(None)) # simplemente representa la ausencia de valor
print(type()) # sin argumentos devuelve None