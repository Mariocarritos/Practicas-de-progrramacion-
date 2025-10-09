# Semana 2 – Condicionales y decisiones en Python

Hola de nuevo, Aaron 👋  
Esta semana vas a aprender a darle **inteligencia a tus programas**: que tomen decisiones según lo que pase.  
Para eso usaremos **condicionales**, que se escriben con la palabra clave `if`.

También vas a aprender a **pedir datos al usuario** usando `input()`.  
Así tus programas podrán interactuar contigo o con otras personas.

---

## 🧠 Conceptos clave

- `input()` sirve para pedirle algo al usuario.
```python
nombre = input("¿Cómo te llamas? ")
```
- if sirve para tomar decisiones:
```python
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

💡 Importante: en Python se usan tabulaciones (sangrías) para indicar qué instrucciones pertenecen a cada bloque.

## 📝 Ejercicio 1: ¿Eres mayor de edad?
👉 Tu misión:

Pide al usuario su nombre.
Pide su edad (recuerda que input() siempre devuelve texto, así que deberás convertirlo a número con int()).
Si la edad es mayor o igual a 18, muestra un mensaje como:

```css
Hola [nombre], eres mayor de edad.
```
Si no, muestra:

```css
Hola [nombre], aún eres menor de edad.
```
### 🎯 Objetivo del ejercicio:

Usar input() para leer datos.
Aprender a convertir texto a número (int()).
Usar if y else para tomar decisiones.

## 📝 Ejercicio 2: Tu primer selector de juegos
👉 Tu misión:
Vas a crear un pequeño programa que recomiende un videojuego según lo que el usuario elija.
Pide al usuario que escriba qué tipo de juego le gusta:
- “peleas”
- “aventura”
- “estrategia”

Usa condicionales (if, elif, else) para mostrar una recomendación según su elección.

Por ejemplo:
- Si elige “peleas”, muestra: Te recomiendo Street Fighter o Mortal Kombat!
- Si elige “aventura”, muestra: Podrías probar Zelda o Hollow Knight!
- Si elige “estrategia”, muestra: Age of Empires siempre es una buena idea!
- Si escribe otra cosa, muestra: No conozco ese tipo de juegos, ¡pero suena interesante!

💡 Pista:
Recuerda que elif significa “si no se cumplió lo anterior, prueba esta otra condición”.

### 🎯 Objetivo del ejercicio:

Comprender cómo funcionan las decisiones múltiples (if, elif, else).
Aprender a combinar texto ingresado por el usuario con lógica condicional.
Entender cómo se comporta un programa interactivo.
