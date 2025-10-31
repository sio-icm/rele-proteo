import RPi.GPIO as GPIO
import time

PIN_RELE = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RELE, GPIO.OUT)

# Desactiva el relé (LOW para la lógica 'Activo en ALTO')
GPIO.output(PIN_RELE, GPIO.LOW)

# Desactiva la configuración de GPIO al salir
GPIO.cleanup() 
print("🔴 Relé ABIERTO (Carga de 24V OFF)")
