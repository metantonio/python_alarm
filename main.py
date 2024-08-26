import time
import datetime
import winsound  # Solo para Windows
import os       # Para sistemas Unix/Linux/Mac

# Configuración de la alarma
intervalo_segundos = 3600  # Intervalo de tiempo en segundos entre cada alarma
repeticiones = 1         # Número de veces que se repetirá la alarma
# Configurar la hora de la alarma (24 horas, formato HH:MM:SS)
hora_objetivo = datetime.time(16, 20, 0)  # 14:30:00 (2:30 PM)


def alarma(intervalo, repeticiones):
    for i in range(repeticiones):
        print(f"Alarma {i + 1}")
        time.sleep(intervalo)
    print("Alarma completada.")




def reproducir_sonido():
    # Windows
    try:
        winsound.Beep(1000, 1000)  # Frecuencia 1000 Hz, duración 1000 ms
    except:
        pass

    # Unix/Linux/Mac
    try:
        os.system('play -nq -t alsa synth 1 sine 1000')
    except:
        pass

def configurar_alarma(hora_objetivo, intervalo, repeticiones):
    
    for i in range(repeticiones):
        print(f'Ejecutándose. \nLa próxima alarma será: {hora_objetivo}')
        while True:
            hora_actual = datetime.datetime.now().time()
            if hora_actual >= hora_objetivo:
                print(f"¡Alarma {i + 1}!")
                reproducir_sonido()
                break
            time.sleep(1)
        
        # Espera el intervalo antes de la próxima alarma
        hora_objetivo = (datetime.datetime.combine(datetime.date.today(), hora_objetivo) +
                         datetime.timedelta(seconds=intervalo)).time()


##alarma(intervalo_segundos, repeticiones)
configurar_alarma(hora_objetivo, intervalo_segundos, repeticiones)
