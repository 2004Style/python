import pyautogui as span
import time

limite = int(input("numero de mensajes: "))
mensaje = input("mensaje: ")

i = 0
time.sleep(5)
while 1 < limite:
    span.typewrite(mensaje)
    span.press('enter')
    i += 1

print("Enviado")