# Import de la librería Tkinter con el nombre "tk"
import tkinter as tk
from tkinter import ttk # ttk contiene el widget Combobox

# Diccionario con unidades y su valor
unidades = {
    "Milímetros": 0.001,
    "Centímetros": 0.01,
    "Metros": 1,
    "Kilómetros": 1000
}

# Ventana principal de la app
ventana = tk.Tk()
ventana.title("CONVERSOR DE UNIDADES SIMPLE") # Título que se muestra en la ventana
ventana.geometry("300x250") # Tamaño anchura x altura en píxeles

# Etiqueta y Campo de entrada
tk.Label(ventana, text="Valor a convertir: ").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Combobox para unidad de origen
tk.Label(ventana, text="Convertir de:").pack(pady=5)
combo_origen = ttk.Combobox(ventana, values=list(unidades.keys()), state="readonly")
combo_origen.current(2) # Valor inicial: "Metros"
combo_origen.pack()

# Combobox para unidad de destino
tk.Label(ventana, text="A: ").pack(pady=5)
combo_destino = ttk.Combobox(ventana, values=list(unidades.keys()), state="readonly")
combo_destino.current(1) # Vloar inicial: "Centímetros"
combo_destino.pack()

# Etiqueta dónde se mostrará el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
resultado.pack(pady=15)

# Función de conversión
def convertir():
    try:
        valor = float(entrada.get())   # lee el número
        unidad_origen = combo_origen.get()
        unidad_destino = combo_destino.get()

        # paso1: convertir todo a metros
        valor_en_metros = valor * unidades[unidad_origen]

        # paso2: pasa de metos a la unidad destino
        resultado_final = valor_en_metros / unidades[unidad_destino]

        resultado.config(
            text=f"{valor} {unidad_origen} = {resultado_final:.4f} {unidad_destino}"
        )   
    except ValueError:
        resultado.config(text="Ingrese un número válido")
        

# Botón convertir
boton = tk.Button(ventana, text="Convertir", command=convertir)
boton.pack(pady=10)

# Bucle principal de la app - mantiene la ventana abierta
ventana.mainloop()
