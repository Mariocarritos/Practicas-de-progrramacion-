# Semana 4 – Listas y colecciones de datos en Python

Hola Aaron 👋
¡Llegaste a un punto muy importante! Esta semana aprenderás a trabajar con listas, una de las estructuras más útiles en programación.

Las listas permiten guardar muchos datos juntos dentro de una sola variable.
Por ejemplo, puedes guardar una lista de nombres, puntajes o incluso tus juegos favoritos.

### 🧠 Conceptos clave
#### 🔹 Qué es una lista

Una lista se escribe entre corchetes [] y sus elementos se separan con comas.


```python
juegos = ["Zelda", "Street Fighter", "Minecraft"]
```

Puedes acceder a cada elemento con su posición (índice), que empieza en 0:

```python
print(juegos[0]) # Muestra "Zelda"
```

También puedes agregar nuevos elementos con append():

```python
juegos.append("God of War")
```

Y recorrer la lista con un bucle for:

```python
for juego in juegos:
print("Juego:", juego)
```

## 📝 Ejercicio 1: Mi lista de juegos favoritos

### 👉 Tu misión:
- Crea un programa que guarde y muestre tus juegos favoritos.
- Crea una lista con al menos 3 juegos que te gusten.

- Muestra en pantalla un mensaje como:
“Mis juegos favoritos son:”

- Luego, usa un bucle for para mostrar cada juego en una línea.
- Al final, agrega un nuevo juego a la lista con append() y muestra la lista actualizada.

### 💡 Pistas:

- Recuerda que append() agrega un nuevo elemento al final de la lista.
- Puedes usar print() dentro del bucle para mostrar cada juego.

### 🎯 Objetivo del ejercicio:

- Comprender cómo crear, recorrer y modificar listas.
- Aprender a combinar listas y bucles for.
- Familiarizarte con los métodos básicos de las listas (append, len, etc.).

## 📝 Ejercicio 2: Tu primer gestor de tareas

### 👉 Tu misión:
- Crea un programa que funcione como un mini gestor de tareas (to-do list).
- Empieza con una lista vacía llamada tareas = [].
- Usa un bucle while para pedir al usuario una tarea con input().
- Cada vez que escriba una tarea, agrégala a la lista.
- Si el usuario escribe "salir", termina el programa.

- Al final, muestra todas las tareas que agregó con un mensaje como: “Tus tareas pendientes son: …”

### 💡 Pistas:

Puedes usar algo así:
```python
while True:
tarea = input("Escribe una tarea (o 'salir' para terminar): ")
if tarea == "salir":
break
tareas.append(tarea)
```

Después del bucle, muestra la lista con un for.

### 🎯 Objetivo del ejercicio:

- Aprender a construir listas dinámicas (que crecen según lo que el usuario hace).
- Combinar bucles, condiciones y listas en un solo programa.
- Empezar a construir programas con flujo real de uso.

✅ Al finalizar la Semana 4, serás capaz de:

- Crear y manipular listas.
- Recorrer elementos de una colección con for.
- Usar bucles while para construir listas a partir de la interacción del usuario.

- Combinar todo lo aprendido hasta ahora para crear tus primeros programas “reales”.

### 💬 Extra (opcional):
Intenta mejorar el gestor de tareas para que:

- Numere cada tarea al mostrarla.
- Permita eliminar tareas escribiendo su número.
- Guarde las tareas iniciales predefinidas (por ejemplo, ["Estudiar", "Entrenar", "Jugar"]).
