# Semana 5 – Funciones en Python 🧩

¡Hola Aaron! 👋
Esta semana vas a aprender a crear funciones, una herramienta clave en programación.

Las funciones te permiten organizar tu código en bloques reutilizables, lo que hace que tus programas sean más ordenados, fáciles de leer y de mantener.
Hasta ahora tus programas corrían de arriba a abajo. Con las funciones, tú decides cuándo y cómo se ejecuta cada parte.

## Conceptos clave
### Qué es una función

Una función es un bloque de código con un nombre, que se ejecuta cuando lo llamas.
Se define con la palabra def:

```python
def saludar():
  print("Hola Aaron, ¡bienvenido al mundo de las funciones!")
```

Para ejecutar la función, simplemente la llamas por su nombre:

```python
saludar()
```

## Funciones con parámetros

También puedes pasarle información a una función:

```python
def saludar(nombre):
  print(f"Hola {nombre}")
```

Cuando la llamas, le pasas un valor:

```python
saludar("Aaron")
```

* Los parámetros son datos que la función necesita para funcionar.

## Funciones que devuelven valores

Una función puede retornar un resultado usando return:

```python
def sumar(a, b):
  return a + b

resultado = sumar(3, 5)
print(f"La suma es: {resultado}")
```

# Ejercicio 1: Tu primer saludo personalizado

## 👉 Tu misión:

Crea una función llamada saludar() que pida el nombre del usuario con input() y luego muestre un saludo.
La función no debe recibir parámetros ni retornar valores, solo mostrar el mensaje.
Llama a la función al final del programa para que se ejecute.

## 💡 Pistas:

Recuerda usar def nombre_funcion(): para definirla.
Puedes combinar input() con print() dentro de la función.

## 🎯 Objetivo del ejercicio:

- Aprender la estructura básica de una función.
- Entender cómo definir y llamar funciones.
- Separar la lógica del programa en bloques.

# Ejercicio 2: Mini calculadora modular

## 👉 Tu misión:
Construir una pequeña calculadora usando funciones.
Define cuatro funciones:

- sumar(a, b)
- restar(a, b)
- multiplicar(a, b)
- dividir(a, b)

Cada función debe retornar el resultado de la operación.
Pide dos números al usuario y una operación (+, -, *, /).
Según la operación elegida, llama a la función correspondiente y muestra el resultado.

## 💡 Pistas:

- Usa if y elif para decidir qué función usar.
- Convierte los números con float() para permitir decimales.
- Asegúrate de que dividir() maneje el caso cuando el divisor sea 0.

## 🎯 Objetivo del ejercicio:

- Aprender a crear funciones reutilizables.
- Comprender cómo pasar datos (parámetros) y obtener resultados (return).
- Combinar condicionales, entrada de usuario y funciones en un mismo flujo.

# Extra (opcional):
- Agrega una nueva función llamada calculadora() que contenga todo el flujo del programa dentro: pedir los números, preguntar la operación y mostrar el resultado. Luego, al final del archivo, solo deberás ejecutar una línea:
