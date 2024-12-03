import time
import datetime
import winsound  # Solo para Windows
import os       # Para sistemas Unix/Linux/Mac
import tkinter as tk
from tkinter import messagebox
import threading

def reproducir_sonido():
    # Windows
    try:
        winsound.Beep(1000, 2000)  # Frecuencia 1000 Hz, duración 2000 ms
    except:
        pass

    # Unix/Linux/Mac
    try:
        os.system('play -nq -t alsa synth 2 sine 1000')
    except:
        pass

def configurar_alarma(hora_objetivo, intervalo, repeticiones):
    # Calcular el primer tiempo objetivo basado en la hora actual
    now = datetime.datetime.now()
    hora_alarma = datetime.datetime.combine(now.date(), hora_objetivo)
    if hora_alarma < now:
        hora_alarma += datetime.timedelta(days=1)

    for i in range(repeticiones):
        print(f'Ejecutándose. \nLa próxima alarma será: {hora_alarma.time()}')

        # Esperar hasta la hora de la alarma
        while True:
            now = datetime.datetime.now()
            if now >= hora_alarma:
                print(f"¡Alarma {i + 1}!")
                reproducir_sonido()
                break
            time.sleep(1)

        # Calcular la próxima hora de alarma
        hora_alarma += datetime.timedelta(seconds=intervalo)

def iniciar_alarma():
    try:
        hora = int(entry_hour.get())
        minuto = int(entry_minute.get())
        if not (0 <= hora <= 23 and 0 <= minuto <= 59):
            raise ValueError
    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, ingrese una hora válida (0-23) y un minuto válido (0-59).")
        return

    hora_objetivo = datetime.time(hora, minuto, 0)
    intervalo_segundos = 3600  # Intervalo de tiempo en segundos entre cada alarma
    repeticiones = 9           # Número de veces que se repetirá la alarma

    root.destroy()  # Cierra la ventana de configuración
    threading.Thread(target=configurar_alarma, args=(hora_objetivo, intervalo_segundos, repeticiones)).start()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Alarma Andrea")

# Establecer el ancho mínimo de la ventana
root.minsize(300, 100)

tk.Label(root, text="Hora (0-23):").grid(row=0, column=0)
entry_hour = tk.Entry(root)
entry_hour.grid(row=0, column=1)

tk.Label(root, text="Minuto (0-59):").grid(row=1, column=0)
entry_minute = tk.Entry(root)
entry_minute.grid(row=1, column=1)

tk.Button(root, text="Iniciar Alarma", command=iniciar_alarma).grid(row=2, columnspan=2)

root.mainloop()
