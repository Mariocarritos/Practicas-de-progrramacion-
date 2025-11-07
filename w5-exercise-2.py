a = float(input("Dame un numero del 1 al 100: "))
b = float(input("Dame un numero del 1 al 100: "))
print("Escoje que haras con esos numeros?")
ecuacion = input("Suma, Resta, Multiplicacion o Division?: ")

#Recuerda las mayusculas y no uses las tildes 


def suma(a, b):
    return a+b
def resta(a, b):
    return a-b 
def multiplicador(a, b):
    return a*b
def dividir(a, b):
    return a/b
if a == 0 or b == 0 and ecuacion == "Division":
    print("El numero 0 no se puede usar para dividir. Reinicie el programa")

elif ecuacion == "Suma":
    print(suma(a, b))
elif ecuacion == "Resta":
    print(resta(a, b))
elif ecuacion == "Multiplicacion":
    print(multiplicador(a, b))
elif ecuacion == "Division":
    print(dividir(a, b))

