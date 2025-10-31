import RPi.GPIO as GPIO
import time

# --- Configuración ---
PIN_RELE = 23  # ¡Cambiado a GPIO 23!

# Usar la numeración de pines BCM (GPIO)
GPIO.setmode(GPIO.BCM) 

# Configurar el pin como SALIDA
GPIO.setup(PIN_RELE, GPIO.OUT)

# Asegurarse de que el relé esté APAGADO inicialmente (HIGH para módulos "Activo en BAJO")
GPIO.output(PIN_RELE, GPIO.HIGH) 

print("Script de control de relé iniciado.")
print(f"El relé está conectado al pin GPIO {PIN_RELE}.")

try:
    # --- Ciclo de prueba ---
    for i in range(3): # Repetir 3 veces
        
        # 1. ACTIVAR el relé (Carga de 24V ENCENDIDA)
        print(f"\n[{i+1}/3] Activando relé (GPIO LOW)...")
        GPIO.output(PIN_RELE, GPIO.LOW) # ¡Bajo voltaje activa el relé!
        time.sleep(3)  # Encendido por 3 segundos

        # 2. DESACTIVAR el relé (Carga de 24V APAGADA)
        print(f"[{i+1}/3] Desactivando relé (GPIO HIGH)...")
        GPIO.output(PIN_RELE, GPIO.HIGH) # Alto voltaje desactiva el relé
        time.sleep(1)  # Apagado por 1 segundo

except KeyboardInterrupt:
    # Detener el script con Ctrl+C
    print("\nPrograma detenido por el usuario.")

finally:
    # Limpiar y asegurar el relé APAGADO al finalizar.
    GPIO.output(PIN_RELE, GPIO.HIGH) 
    GPIO.cleanup()
    print("Limpieza de GPIO completada. Relé asegurado en estado OFF.")
