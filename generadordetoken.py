import random
import string


def main():
    # Definir los caracteres permitidos
    chars = string.ascii_letters + string.digits

    # Generar un token de al menos 6 caracteres
    token = "".join(random.choice(chars) for _ in range(6))

    # Mostrar el token generado
    print("Token generado:", token)

if __name__ == "__main__":
    main()
