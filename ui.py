import time
import datetime
import winsound  # Solo para Windows
import os       # Para sistemas Unix/Linux/Mac
import tkinter as tk
from tkinter import messagebox


def reproducir_sonido():
    # Windows
    try:
        winsound.Beep(1000, 2000)  # Frecuencia 1000 Hz, duración 2000 ms
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
    configurar_alarma(hora_objetivo, intervalo_segundos, repeticiones)


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
