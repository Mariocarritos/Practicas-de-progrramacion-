import random
secreto = random.randint(1,10)
print("Vamos a jugar a adivinar un numero del 1 al 10!")
intento = int(input("Escoge un numero del 1 al 10: "))

#Forma 1

while secreto != intento:
    if intento < secreto:
        print("Ups! El numero es demaciado bajo :(")
        intento = int(input("Vuelve a intentarlo: "))
    elif intento > secreto:
        print("Casi! El numero es demaciado alto >:v")
        intento = int(input("Vuelve a intentarlo: "))

print("Adivinaste el numero secreto :P!")
    

juego2 = random.randint(1,20)
print("Vamos a subir la dificultad, ahora es un numero del 1 al 20!")
intento2 = int(input("Escoge un numero del 1 al 20: "))

#Forma 2

while intento2 < juego2 or intento > juego2:
    if intento2 < juego2:
        print("Ups! El numero es demaciado bajo :(")
        intento2 = int(input("Vuelve a intentarlo: "))
    elif intento2 > juego2:
        print("Casi! El numero es demaciado alto >:v")
        intento2 = int(input("Vuelve a intentarlo: "))

print("Adivinaste el numero secreto por segunda vez :P!")
