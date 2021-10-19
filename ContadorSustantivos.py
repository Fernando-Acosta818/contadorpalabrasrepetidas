# Contador de repetición de palabras
# Versión 1:

# Problemas sin solucionar:

# El usuario debe ingresar siempre el nombre
# correcto del archivo.

# Las palabras cortas como nexos o pronombres
# son erróneamente contadas. ej: "la" en "labio".

# El programa termina y debe reiniciarse para
# hacer otra consulta.

# No hay interfaz gráfica.

filename = input("Inserta el nombre del archivo: ")
file = open(filename)
word = input("Palabra: ")
lword = word.lower()
total = 0

for lines in file :
    lines = lines.lower()
    total = total + lines.count(lword)

print(word, "está escrito", total, "veces en el texto.")
