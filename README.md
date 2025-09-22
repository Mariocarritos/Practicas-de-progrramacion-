# Semana 1 – Tipos de datos en Python

Bienvenido Aaron 👋  
En esta primera semana aprenderás a trabajar con **tipos de datos básicos en Python**:  
- **Números** (enteros y decimales)  
- **Cadenas de texto** (strings)  
- **Valores lógicos** (booleanos: `True` o `False`)  

Vas a resolver **2 ejercicios** que te ayudarán a practicar y entender cómo usar estos datos en programas simples.

- Deberás crear 2 archivos `.py`, `exercise-1.py` y `exercise-2.py`, y en cada uno escribir tu código python con la solución a cada ejercicio.

## 📝 Ejercicio 1: Conociendo a las variables

En programación, una **variable** es como una caja en la que guardamos un dato con un nombre.  
Ese dato puede ser un número, un texto o un valor lógico.

👉 **Tu misión:**  
1. Crea una variable que guarde tu **nombre**.
2. Crea una variable que guarde tu **edad**.
3. Crea una variable que guarde tu **videojuego favorito**.
4. Haz que Python muestre en pantalla una frase usando esas variables.

💡 **Pista**: Para mostrar texto en Python se usa la función `print()`.    
```python
print("Hola, soy Aaron")
```
Cuando uses variables, puedes combinarlas con texto usando f-strings , antepondiendo la letra 'f' antes del string:

```python
print(f"Mi nombre es {nombre}")
```

🎯 Objetivo del ejercicio:

- Practicar cómo crear variables.
- Diferenciar entre texto (strings) y números (int).
- Aprender a mostrar información en pantalla con print().

📝 Ejercicio 2: Tu primer mini-calculadora
Ahora que sabes usar variables, vas a crear un programa que funcione como una mini calculadora.

👉 Tu misión:

- Crea dos variables que guarden números (puedes elegirlos tú).
- Haz que Python muestre la suma de esos dos números.
- Haz que muestre también la resta, la multiplicación y la división.
- Agrega un mensaje explicativo para cada operación, por ejemplo:
  - `"La suma es: ..."`
  - `"La resta es: ..."`

💡 Pista:
En Python puedes usar:

- `+` para sumar
- `-` para restar
- `*` para multiplicar
- `/` para dividir

Ejemplo básico:

```python
resultado = 5 + 3
print("El resultado es", resultado)
```

🎯 Objetivo del ejercicio:

- Practicar cómo usar números en Python.
- Aprender operaciones básicas.
- Empezar a pensar cómo los programas pueden hacer cálculos automáticamente.
