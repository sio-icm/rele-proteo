import RPi.GPIO as GPIO
import time

PIN_RELE = 23
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RELE, GPIO.OUT)

# Activa el relé (HIGH para la lógica 'Activo en ALTO' de tu módulo)
GPIO.output(PIN_RELE, GPIO.HIGH) 

# El mensaje debe ser: CERRADO (Encendido)
print("🟢 Relé CERRADO (Carga de 24V ON)")
