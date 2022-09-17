#  ______      _        _         ___
# /_  __/____ (_)_  __ (_)___ _  / _ \ ____ ___  ___ _ ____ ___ _ __ _
#  / /  / __// /| |/ // // _ `/ / ___// __// _ \/ _ `// __// _ `//  ' \
# /_/  /_/  /_/ |___//_/ \_,_/ /_/   /_/   \___/\_, //_/   \_,_//_/_/_/
#                                              /___/

from time import sleep
from os import system, name
from random import randint
from pick import pick


# Function para limpiar la console
def clear():
    command = "clear"
    if name in ('nt', 'dos'):
        command = "cls"
    system(command)


# Bienvenida para el juego
title = "Bienvenido a esta Trivia, Desea jugar? "
options = ['Si!', 'No!']
selected = pick(options, title, multiselect=False, min_selection_count=1)

if selected[0] == "Si!":
    # Iniciamos variables de contador
    score = randint(0, 11)
    intento = 0

    # Pedimos el nombre del usuario y le mostramos su puntuación inicial
    clear()
    name = input("Ahora dime tu nombre?: ")

    while True:
        # Bienvenida del juego
        intento += 1  # Aumentamos el numero de intentos
        print("\033[32m" + f"Okay {name}, tu puntuación actual es: {score}\n" +
              "\033[00m")
        print(f"Este es tu intento numero {intento}")
        sleep(2)
        clear()

        # ! Primera pregunta
        print("""
   ¿Cuál es el lugar más frío de la tierra?

A) Rusia.
B) Antártida.
C) Groenlandia.
D) Estonia.
""")
        res = input("Inserte la respuesta: ").lower()

        # Comprobamos si la entrada es la esperada
        while res not in ("a", "b", "c", "d"):
            res = input("\033[31m" + "Escribe una respuesta correcta: " +
                        "\033[00m").lower()

        # Comprobamos si la respuesta es correcta
        if res == "a":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "b":
            score += 5  # Te suma puntos si es correcta
            print(
                "\033[32m" +
                f"Correcta {name}! Se te han sumado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "c":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "d":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")

        # Esperamos para cargar la siguiente pregunta y limpiamos
        sleep(3)
        clear()

        # ! Segunda pregunta
        print("""
   ¿Cuál es el río más largo del mundo?

A) Misisipi
B) Nilo
C) Yangtsé
D) Amazonas
""")
        res = input("Inserte la respuesta: ").lower()

        # Comprobamos si la entrada es la esperada
        while res not in ("a", "b", "c", "d"):
            res = input("\033[31m" + "Escribe una respuesta correcta: " +
                        "\033[00m").lower()

        # Comprobamos si la respuesta es correcta
        if res == "a":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "b":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "c":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "d":
            score += 5  # Te suma puntos si es correcta
            print(
                "\033[32m" +
                f"Correcta {name}! Se te han sumado puntos, Tu puntuación actual es {score}"
                + "\033[00m")

        # Esperamos para cargar la siguiente pregunta y limpiamos
        sleep(3)
        clear()

        # ! Tercera pregunta
        print("""
   ¿Què cantidad de huesos en el cuerpo humano Adulto?

A) 206
B) 250
C) 300
D) 189
""")
        res = input("Inserte la respuesta: ").lower()

        # Comprobamos si la entrada es la esperada
        while res not in ("a", "b", "c", "d"):
            res = input("\033[31m" + "Escribe una respuesta correcta: " +
                        "\033[00m").lower()

        # Comprobamos si la respuesta es correcta
        if res == "a":
            score += 5  # Te suma puntos si es correcta
            print(
                "\033[32m" +
                f"Correcta {name}! Se te han sumado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "b":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "c":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "d":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")

        # Esperamos para cargar la siguiente pregunta y limpiamos
        sleep(3)
        clear()

        # ! Cuarta pregunta
        print("""
   ¿Cuándo acabó la II Guerra Mundial?

A) 1910
B) 1876
C) 1945
D) 1923
""")
        res = input("Inserte la respuesta: ").lower()

        # Comprobamos si la entrada es la esperada
        while res not in ("a", "b", "c", "d"):
            res = input("\033[31m" + "Escribe una respuesta correcta: " +
                        "\033[00m").lower()

        # Comprobamos si la respuesta es correcta
        if res == "a":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "b":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "c":
            score += 5  # Te suma puntos si es correcta
            print(
                "\033[32m" +
                f"Correcta {name}! Se te han sumado puntos, Tu puntuación actual es {score}"
                + "\033[00m")
        elif res == "d":
            score -= 5  # Te resta puntos si es incorrecta
            print(
                "\033[31m" +
                f"Incorrecto {name}! Se te han restado puntos, Tu puntuación actual es {score}"
                + "\033[00m")

        # Esperamos para cargar la siguiente pregunta y limpiamos
        sleep(3)
        clear()

        # Condición que comprueba si tu puntaje es mejor o menor a 0 y te da un color
        if score > 0:
            print("\033[32m" + f"Tu puntuación Final es {score}" + "\033[00m")

            sleep(5)
        else:
            print("\033[31m" + f"Tu puntuación Final es {score}\n" +
                  "\033[00m")
            print(
                "Como tu puntuación es negativa te vamos a otorgar un bonus\n")
            bonus = int(input("Ingresa un numero: "))

            # Mensaje secreto
            if bonus == 1998:
                print("En este año se descubrió la inyección SQL")
                sleep(5)
                clear()
            else:
                print(
                    f"Tu puntuación paso de ser {score} a ser: {score + bonus}"
                )
                sleep(5)
                clear()

        # Sistema de repetición
        clear()
        title = "Desea repetir el juego?: "
        options = ['Si!', 'No!']
        selected = pick(options,
                        title,
                        multiselect=False,
                        min_selection_count=1)

        if selected[0] == "Si!":
            score = 0
            continue
        else:
            # Despedida en caso de que no se quiera continuar
            print(
                f"Espero que te haya gustado {name}, espero que vuelvas proto ^^\n"
            )
            print("\033[31m" + "Saliendo..." + "\033[00m")
            sleep(2)
            break

elif selected[0] == "No!":
    print("\033[31m" + "Cerrando el programa..." + "\033[00m")
    sleep(3)
    exit(0)
