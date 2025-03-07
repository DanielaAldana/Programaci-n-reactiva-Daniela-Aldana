import rx
from rx import operators as ops
import rx.operators as ops
import time
import random

# Función para simular la lectura de un sensor de temperatura
def leer_sensor():
    return round(random.uniform(30, 42), 2)  # Temperatura entre 30°C y 42°C

# Crear un flujo reactivo que emite una lectura cada segundo
sensor_temperatura = rx.interval(1).pipe(
    ops.map(lambda _: leer_sensor()),  # Leer sensor
    ops.do_action(lambda t: print(f"🌡 Temperatura actual: {t}°C")),  # Mostrar lectura
    ops.filter(lambda t: t > 38)  # Filtrar temperaturas peligrosas
)

# Suscribirse al flujo de eventos y actuar si hay temperaturas altas
sensor_temperatura.subscribe(
    on_next=lambda t: print(f"🚨 ALERTA: ¡Temperatura alta detectada! {t}°C"),
    on_error=lambda e: print(f"⚠️ Error: {e}"),
    on_completed=lambda: print("✅ Monitoreo finalizado.")
)

# Mantener el programa corriendo
time.sleep(10)  # Ejecuta durante 10 segundos antes de finalizar