import math
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def utilizar_perceptron (inp, out):
    while True:
        sesgo = float(input ("Ingrese el valor de sesgo: "))
        pesos = []
        for i in range (len(inp)):
            pesos.append(float(input("Ingrese un valor de peso para X"+str(i+1)+": ")))
        z = suma_ponderada (inp, pesos, sesgo)
        opcion = int(input ("1. Escalon\n2. Sigmoide\nElija una opcion:"))
        if opcion == 1:
            predic = escalon(z)
            graficar (inp, out, predic, "escalon")
        elif opcion == 2:
            predic = sigmoide (z)
            graficar (inp, out, predic, "sigmoide")
        
        

        opcion = input ("Desea cambiar los valores (s/n): ")
        if opcion == "n":
            break

def suma_ponderada (inp, pesos, sesgo):
    z = []
    for i in range (len (inp[0])):
        aux = 0
        for j in range (len (inp)):
            aux += ((inp[j][i]) * (pesos[j]))
        aux += sesgo
        z.append (aux)
    return z

def escalon (z):
    output = []
    for i in range (len(z)):
        if z[i] >= 0:
            output.append(1)
        else:
            output.append(0)
    return output

def sigmoide (z):
    output = []
    for i in range (len(z)):
        output.append (round(1/(1+math.exp(-z[i])),4))
    return output

def graficar(A, out, predict, funcion_activacion):
    n = len(out)
    delta = 0.1  
    def clasificar_y(y):
        if funcion_activacion == "escalon":
            return y
        elif funcion_activacion == "sigmoide":
            return 1 if y >= 0.5 else 0

    predict_clasificado = [clasificar_y(y) for y in predict]

    fig, axes = plt.subplots(1, 3, figsize=(18,6)) 

    axes[0].scatter(A[0], A[1], c='black', s=50)  
    for i in range(n):
        axes[0].text(A[0][i], A[1][i]+delta, str(out[i]), color='black',
                     fontsize=12, ha='center', va='bottom')
    axes[0].set_title("Valores esperados")
    axes[0].set_xlabel("X1")
    axes[0].set_ylabel("X2")
    axes[0].grid(True)

    axes[1].scatter(A[0], A[1], c='black', s=50)  
    for i in range(n):
        axes[1].text(A[0][i], A[1][i]+delta, str(predict_clasificado[i]), color='black',
                     fontsize=12, ha='center', va='bottom')
    axes[1].set_title("Valores predichos")
    axes[1].set_xlabel("X1")
    axes[1].set_ylabel("X2")
    axes[1].grid(True)

    for i in range(n):
        color = 'green' if out[i] == predict_clasificado[i] else 'red'
        axes[2].scatter(A[0][i], A[1][i], c=color, s=100)
    axes[2].set_title("Coincidencias")
    axes[2].set_xlabel("X1")
    axes[2].set_ylabel("X2")
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()