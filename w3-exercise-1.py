num = int(input("Escoje un numero del 1 al 30: "))

if num <= 30 and num > 0:
    for i in range(num):
        print("Repeticion numero", i + 1)
        print(f"Yyyyyyy... ¡Listo!. Conté hasta el numero {num}")
else:
    print("El numero no se puede usar. Por favor reinicie el programa")


