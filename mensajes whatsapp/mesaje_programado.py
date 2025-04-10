import pyautogui as span
import time
from datetime import datetime

# Obtener la hora de envío definida por el usuario
hora_envio = input("Introduce la hora de envío en formato HH:MM (24 horas): ")
#mensaje = "buenos dias ojitos lindos espero hayas tenido un hermoso descansar y estes con muchas energias y espero que tengas un bonito dia asi como tu y si amaneciste triste te mando un fuerte abrazo porque una chica hermosa como tu tiene que estar bien y con muchos animos te quiero mucho mi bonita"
mensaje = input("ingresar mensaje: ")

# Parsear la hora de envío
hora_objetivo = datetime.strptime(hora_envio, "%H:%M").time()


# Función que espera hasta la hora definida
def esperar_hora_objetiva(hora_objetivo):
    while True:
        ahora = datetime.now().time()
        if ahora >= hora_objetivo:
            break
        time.sleep(30)  # Espera 30 segundos antes de volver a comprobar


# Espera hasta la hora establecida
print(f"Esperando hasta las {hora_envio} para enviar el mensaje...")
esperar_hora_objetiva(hora_objetivo)

# Enviar el mensaje
span.typewrite(mensaje)
span.press("enter")

print("Mensaje enviado")
