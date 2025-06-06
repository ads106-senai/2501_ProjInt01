import time
import tkinter as tk
from datetime import datetime
from clp import CLP

# Como executar a cada 5 seg por tempo 
myclp = CLP('192.168.0.103')
myclp.connect()

# running controla se o monitoramento está funcionando
running = False

# Cria a tela
root = tk.Tk()
root.title("Monitoramento CLP")
root.geometry("400x300")

# Função executada pelo botão Start
def startRunning():
    global running
    running = True
    # Inicia um temporizador de 1000ms (1s)
    root.after(1000, update)

# Função executada pelo botão Stop
    
def stopRunning():
    global running
    running = False    

btStart = tk.Button(root, text="Start", command=startRunning)
btStart.grid(row=1, column=1, columnspan=1)
btStop  = tk.Button(root, text="Stop", command=stopRunning)
btStop.grid(row=1, column=2, columnspan=1)
tk.Label(root, text="Timestamp").grid(row=2, column=1, columnspan=1)
txtTime = tk.Label(root, text=f"{datetime.now().strftime('%H:%M:%S')}", wraplength=300)
txtTime.grid(row=2, column=2, columnspan=1)
tk.Label(root, text="VALUE").grid(row=3, column=1, columnspan=1)
txtValue = tk.Label(root, text="0000", wraplength=300)
txtValue.grid(row=3, column=2, columnspan=1)
root.grid_columnconfigure(4, minsize=200)


# Função executado pelo temporizador (a cada 1s)
def update():
    global myCLP
    global btValue
    global running

    # Executará novamente daqui 1s se running ainda for True
    if (running):
        root.after(1000, update)

    # Lê CLP e armazena valor no objeto txtValue
    resultado=myclp.read("Local:4:I.Ch0Data")
    txtTime.config(text= f"{datetime.now().strftime('%H:%M:%S')}")
    txtValue.config(text= f"{resultado.value}")

root.mainloop()


