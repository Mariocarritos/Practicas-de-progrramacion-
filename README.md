# Semana 3 – Bucles en Python (Repeticiones y automatización)

Hola Aaron 👋
En esta oportunidad aprenderás a usar los bucles, una de las herramientas más poderosas en programación.
Los bucles permiten que el código repita una acción muchas veces sin escribirla manualmente.

En Python hay dos tipos principales de bucles:

* for → cuando sabes cuántas veces quieres repetir algo.

* while → cuando quieres repetir algo hasta que se cumpla una condición.

## 🧠 Conceptos clave
### Bucle for

Sirve para recorrer una secuencia (como una lista o un rango de números):

```python
for i in range(5):
  print("Repetición número", i)
```

Esto imprime del 0 al 4.
range(5) crea una secuencia de 5 números.

### Bucle while

Repite algo mientras una condición sea verdadera:

```python
contador = 0
while contador < 5:
  print("Contador:", contador)
  contador += 1
```

El bucle se detiene cuando contador deja de ser menor que 5.

## 📝 Ejercicio 1: Contador divertido

👉 Tu misión:

- Pide al usuario un número con input().
- Usa un bucle for para contar desde 1 hasta ese número, mostrando cada número en pantalla.
- Al final del conteo, muestra un mensaje como:
´´´css
¡Listo! Conté hasta [número].
´´´

### 💡 Pistas:

- Recuerda que range(1, numero + 1) cuenta desde 1 hasta el número ingresado.
- No olvides convertir el valor ingresado con int().

## 🎯 Objetivo del ejercicio:

- Entender cómo funciona for y el objeto range().
- Practicar la conversión de texto a número.
- Empezar a combinar entrada de usuario con repeticiones.

## 📝 Ejercicio 2: Adivina el número secreto

### 👉 Tu misión:

Crea un pequeño juego donde el programa elija un número secreto (por ejemplo, 7) y el jugador deba adivinarlo.

- Define una variable secreto = 7.
- Pide al usuario que adivine el número.
- Usa un bucle while que siga pidiendo intentos hasta que el jugador acierte.
- Si el número ingresado es menor al secreto, muestra "Demasiado bajo".
- Si es mayor, muestra "Demasiado alto".
- Cuando el jugador acierte, muestra "¡Adivinaste el número secreto!".

### 💡 Pistas:

- Usa int() para convertir la respuesta a número.
- Dentro del bucle, puedes actualizar la variable con un nuevo input() cada vez.

## 🎯 Objetivo del ejercicio:

- Comprender cómo funcionan los bucles while.
- Controlar cuándo detener un bucle.
- Aplicar condiciones (if) dentro de un bucle.

# 💬 Extra (opcional):
Haz que el número secreto sea aleatorio usando el módulo random:

```python
import random
secreto = random.randint(1, 10)
```
