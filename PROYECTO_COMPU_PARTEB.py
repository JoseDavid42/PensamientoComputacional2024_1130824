import time
import random
from datetime import datetime

zonas = {}
temperatura_actual = {}
temperatura_deseada = {}
horario = {}
logs = []

def Agregar_Zona(zona):
    if zona and zona not in zonas:
        zonas[zona] = 22
        temperatura_actual[zona] = 22
        temperatura_deseada[zona] = 22
        log(f"{zona} agregada con 22°C")

def Ajustar_Temperatura(zona, temperatura):
    if zona in zonas:
        temperatura_deseada[zona] = temperatura
        log(f"La temperatura de {zona} fue ajustada a {temperatura} °C")

def Establecer_horario(zona, temperatura, hora):
    try:
        hora = datetime.strptime(hora, "%H:%M").time()
        if zona in zonas:
            horario[hora] = (zona, temperatura)
            log(f"Programado! {zona} estará a {temperatura} °C a las {hora}")
        else:
            log(f"Zona {zona} no existe.")
    except ValueError:
        log("Sintaxis inválida, escribe bien la hora :)")

def log(mensaje):
    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {mensaje}"
    logs.append(log_entry)
    print(log_entry)

def Monitor_Principal():
    global temperatura_actual, temperatura_deseada
    hora_actual = datetime.now().time()
    for zona in zonas:
        temperatura_actual_local = temperatura_actual[zona]
        temperatura_deseada_local = temperatura_deseada.get(zona, 22)

        temperatura_actual_local += random.uniform(-0.5, 0.5)
        temperatura_actual[zona] = temperatura_actual_local

        if temperatura_actual_local < temperatura_deseada_local:
            temperatura_actual[zona] += 1
        elif temperatura_actual_local > temperatura_deseada_local:
            temperatura_actual[zona] -= 1

        log(f"{zona} : Temperatura: {temperatura_actual[zona]:.1f}°C , Temperatura deseada: {temperatura_deseada_local}°C")

    for hora, (zona, temperatura) in horario.items():
        if hora.hour == hora_actual.hour and hora.minute == hora_actual.minute:
            temperatura_deseada[zona] = temperatura
            log(f"Alarma: {zona} a {temperatura}°C")

def main():
    print("Hola! Bienvenido a HSmart el mejor sistema de automatización")
    while True:
        print("Opciones")
        print("1. Configuración de Zonas")
        print("2. Control de temperaturas")
        print("3. Horarios")
        print("4. Registro")
        print("5. Salir")
        opcion = input("Seleccione la opción que desee: ")

        if opcion == "1":
            zona = input("Ingrese el nombre de la zona que desea: ")
            Agregar_Zona(zona)
        elif opcion == "2":
            zona = input("Ingrese el nombre de la zona que desea: ")
            temperatura = int(input("Ingrese la temperatura deseada: "))
            Ajustar_Temperatura(zona, temperatura)
        elif opcion == "3":
            zona = input("Ingrese el nombre de la zona que desea: ")
            temperatura = int(input("Ingrese la temperatura deseada: "))
            hora = input("Ingrese la hora (HH:MM) que desea programarlo: ")
            Establecer_horario(zona, temperatura, hora)
        elif opcion == "4":
            print("REGISTRO:")
            print(" ")
            for log_entry in logs:
                print(log_entry)
        elif opcion == "5":
            print("Saliendo...")
            print("Gracias por hacer uso de nuestro sistema, vuelva pronto")
            break
        else:
            print("Opción inválida, intente de nuevo")

        Monitor_Principal()
        time.sleep(0.75)

main()
