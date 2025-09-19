from funciones import *
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

while True:
    print("\n===Bienvenido a la tarea 1===\n\n1. Utilizar perceptron\n2. Salir")
    opcion = input("\nElige una opcion: ")
    
    if opcion == "1":

        ruta_archivo = filedialog.askopenfilename(
            title="Selecciona un archivo CSV",
            filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
        )
        if not ruta_archivo:
            print("No se seleccionó ningún archivo")
            continue

        inp = []
        out = []

        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for _ in range(len(lineas[1].strip().split(",")) - 1):
                inp.append([])
            for linea in lineas[1:]:
                valores = linea.strip().split(",")
                for i in range(len(valores)-1):
                    inp[i].append(float(valores[i]))
                out.append(float(valores[-1]))
        

        utilizar_perceptron(inp, out)
    
    elif opcion == "2":
        print("salir")
        break
    else:
        print("Elige opcion valida\n")