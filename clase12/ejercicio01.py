"""
Hacer un script donde se cree un archivo prueba.txt y
se escriba dentro en dos líneas vuestro nombre y en la 
siguiente línea que estáis estudiando python
posteriormente, intentad leedlo en el mismo script, 
deberías verlo como dos lineas
puntos extra si después de ver que funciona cambiáis algo
del texto y lo leeis, y veis el cambio
"""
# 1. Crear y escribir las dos líneas iniciales en el archivo
archivo = open("prueba.txt", "w")
archivo.write("Ricardo Lamelas\n")
archivo.write("Estoy estudiando Python\n")

# 2. Leer el archivo y mostrarlo como dos líneas
archivo = open("prueba.txt", "r")
for linea in archivo:
    print(linea.strip())

# 3. Modificar el texto del archivo (Puntos extra)
archivo = open("prueba.txt", "r")
contenido = archivo.read()

contenido_modificado = contenido.replace("Python", "programación en Python")

archivo = open("prueba.txt", "w")
archivo.write(contenido_modificado)

# 4. Volver a leer el archivo para comprobar el cambio
archivo = open("prueba.txt", "r")
for linea in archivo:
    print(linea.strip())
