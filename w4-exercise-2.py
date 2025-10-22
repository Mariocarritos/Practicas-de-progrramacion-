tarea = []

while True:
    preg = input("Anota una tarea que nececites recordar(o Salir para cerrar el programa): ")
    if preg == "Salir":
        break
    else:
        tarea.append(preg)
        print(tarea)


