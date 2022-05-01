
from random import *
nombre_usuario=input("¿Nombre?\n").lower()
print(f"{nombre_usuario},he pensado un número aleatorio entre el 1 y el 10, intenta averiguarlo:\n")
aleatorio=randint(1,10)
respuesta = ""
contador=0
contador_atras=8
while respuesta != aleatorio:
    contador_atras=contador_atras-1
    respuesta=int(input("Introduce un número entre 1 y 10:\n"))
    print(f"¡TE QUEDAN {contador_atras} INTENTOS!")
    contador=contador+1
    if respuesta==aleatorio:
        print("¡HAS GANADO!")
        break
    elif contador>=8:
        print("¡PERDISTE!, ¡HAS SUPERADO EL NUMERO DE INTENTOS!")
        break
    elif respuesta<1 or respuesta>10:
        print("¡NUMERO NO PERMITIDO!")
    elif respuesta>aleatorio:
        print("¡HAS INTRODUCIDO UN NUMERO MAYOR AL NUMERO AL NUMERO SECRETO!")
    elif respuesta<aleatorio:
        print("¡HAS INTRODUCIDO UN NUMERO MENOR AL NUMERO AL NUMERO SECRETO!")
else:
    print("")
