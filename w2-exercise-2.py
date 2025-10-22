print("Quieres conocer juegos de tu genero favorito?")
print("Escribe tu genero de videojuegos favorito y te recomendare varios del mismo genero")
genero = input("Escoge entre: Aventura, RPG, Estrategia o Peleas: ")

#Recuerda la mayusculas

if genero == "Aventura":
    print("Podrías probar Zelda o Hollow Knight!")
elif genero == "RPG":
    print("Podrías probar Undertale o EarthBound!")
elif genero == "Estrategia":
    print("Age of Empires y Clash Royale siempre son una buena idea!")
elif genero == "Peleas":
    print("Te recomiendo Street Fighter, Mortal Kombat o Dragon ball fighter Z!")
else:
    print("No conozco ese tipo de juegos, ¡pero suena interesante!")