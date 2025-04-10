import random

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataqueMAX = random.randint(20, 100)
        self.vidaMAX = random.randint(150, 400)
        self.vidaACTUAL = self.vidaMAX

    def __str__(self):
        return f'Pokemon: {self.nombre}, Ataque Máximo: {self.ataqueMAX}, Vida Máxima: {self.vidaMAX}, Vida Actual: {self.vidaACTUAL}'

def crearEntrenadorPokemon(numero_entrenador):
    nombre_entrenador = input(f'Ingrese el nombre del entrenador {numero_entrenador}: ')
    nombre_pokemon = input(f'Ingrese el nombre del pokemon del entrenador {numero_entrenador}: ')
    return Entrenador(nombre_entrenador), Pokemon(nombre_pokemon)

def valorDeAtaque(pokemon):
    return random.randint(0, pokemon.ataqueMAX)

def defender(pokemon, ataque):
    esquiva = random.randint(1, 6)
    if esquiva == 6:
        ataque_recibido = 0
    else:
        ataque_recibido = ataque
    pokemon.vidaACTUAL = max(0, pokemon.vidaACTUAL - ataque_recibido)

def recuperar(pokemon):
    pokemon.vidaACTUAL = pokemon.vidaMAX

def main():
    print("¡Bienvenido a la batalla Pokemon!")
    primerentrenador, primerpokemon = crearEntrenadorPokemon(1)
    
    victorias = 0
    derrotas = 0

    while True:
        print("\n¡Comienza la batalla Pokemon!")

        segundoentrenador, segundopokemon = crearEntrenadorPokemon(2)

        print(f'\nEstadísticas de {primerpokemon.nombre}:')
        print(primerpokemon)
        print(f'\nEstadísticas de {segundopokemon.nombre}:')
        print(segundopokemon)

        recuperar(primerpokemon)
        recuperar(segundopokemon)

        while True:
            opcion = input("\n¿Desea pelear (P) o finalizar el juego (F)? ").upper()
            if opcion == 'P':
                ataque_primerpokemon = valorDeAtaque(primerpokemon)
                defender(segundopokemon, ataque_primerpokemon)

                ataque_segundopokemon = valorDeAtaque(segundopokemon)
                defender(primerpokemon, ataque_segundopokemon)

                print(f'\n{primerpokemon.nombre} ataca a {segundopokemon.nombre} y le causa {ataque_primerpokemon} de daño.')
                print(f'Vida Actual de {segundopokemon.nombre}: {segundopokemon.vidaACTUAL}')
                print(f'\n{segundopokemon.nombre} ataca a {primerpokemon.nombre} y le causa {ataque_segundopokemon} de daño.')
                print(f'Vida Actual de {primerpokemon.nombre}: {primerpokemon.vidaACTUAL}')

                if segundopokemon.vidaACTUAL <= 0:
                    print(f'\n{primerentrenador} y {primerpokemon.nombre} ganan la batalla!')
                    victorias += 1
                    break
                elif primerpokemon.vidaACTUAL <= 0:
                    print(f'\n{segundoentrenador} y {segundopokemon.nombre} ganan la batalla!')
                    derrotas += 1
                    break

            elif opcion == 'F':
                print("\nJuego terminado.")
                print(f'Estadísticas de {primerentrenador} y su Pokemon:')
                print(f'Victorias: {victorias}, Derrotas: {derrotas}')
                return
            else:
                print("Opción no válida. Por favor, ingrese 'P' para pelear o 'F' para finalizar el juego.")

if __name__ == "__main__":
    main()
