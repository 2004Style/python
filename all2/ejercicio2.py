#!/usr/local/bin/python
# coding: latin-1


import random

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque_maximo = random.randint(20, 100)
        self.vida_maxima = random.randint(150, 400)
        self.vida_actual = self.vida_maxima

    def __str__(self):
        return f'Pokemon: {self.nombre}, Ataque M�ximo: {self.ataque_maximo}, Vida M�xima: {self.vida_maxima}, Vida Actual: {self.vida_actual}'

def crearEntrenadorPokemon(numero_entrenador):
    nombre_entrenador = input(f'Ingrese el nombre del entrenador {numero_entrenador}: ')
    nombre_pokemon = input(f'Ingrese el nombre del pokemon del entrenador {numero_entrenador}: ')
    return Entrenador(nombre_entrenador), Pokemon(nombre_pokemon)

def valorDeAtaque(pokemon):
    return random.randint(0, pokemon.ataque_maximo)

def defender(pokemon, ataque):
    esquiva = random.randint(1, 6)
    if esquiva == 6:
        ataque_recibido = 0
    else:
        ataque_recibido = ataque
    pokemon.vida_actual = max(0, pokemon.vida_actual - ataque_recibido)

def recuperar(pokemon):
    pokemon.vida_actual = pokemon.vida_maxima

def resetearPokemon(pokemon):
    recuperar(pokemon)

def crearNuevoOponente(numero_oponente):
    print(f'\nPreparando oponente {numero_oponente}...')
    print(f'\n�Comienza la batalla de entrenadores y sus Pokemon!')

def main():

    entrenador1, pokemon1 = crearEntrenadorPokemon(1)
    
    victorias = 0
    derrotas = 0

    while True:
        crearNuevoOponente(victorias + derrotas + 1)

        entrenador2, pokemon2 = crearEntrenadorPokemon(2)

        print(f'\nEstad�sticas de {pokemon1.nombre}: ')
        print(pokemon1)
        print(f'\nEstad�sticas de {pokemon2.nombre}: ')
        print(pokemon2)

        resetearPokemon(pokemon1)

        while True:
            opcion = input("\n�Desea pelear (P) o finalizar el juego (F)? ").upper()
            if opcion == 'P':
                ataque_pokemon1 = valorDeAtaque(pokemon1)
                defender(pokemon2, ataque_pokemon1)

                ataque_pokemon2 = valorDeAtaque(pokemon2)
                defender(pokemon1, ataque_pokemon2)

                print(f'\n{pokemon1.nombre} ataca a {pokemon2.nombre} y le causa {ataque_pokemon1} de da�o.')
                print(f'Vida Actual de {pokemon2.nombre}: {pokemon2.vida_actual}')
                print(f'\n{pokemon2.nombre} ataca a {pokemon1.nombre} y le causa {ataque_pokemon2} de da�o.')
                print(f'Vida Actual de {pokemon1.nombre}: {pokemon1.vida_actual}')

                if pokemon2.vida_actual <= 0:
                    print(f'\n{entrenador1} y {pokemon1.nombre} ganan la batalla!')
                    victorias += 1
                    break
                elif pokemon1.vida_actual <= 0:
                    print(f'\n{entrenador2} y {pokemon2.nombre} ganan la batalla!')
                    derrotas += 1
                    break

            elif opcion == 'F':
                print("\nJuego terminado.")
                print(f'Estad�sticas de {entrenador1} y su Pokemon:')
                print(f'Victorias: {victorias}, Derrotas: {derrotas}')
                return
            else:
                print("Opci�n no v�lida. Por favor, ingrese 'P' para pelear o 'F' para finalizar el juego.")

main()