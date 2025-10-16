import tkinter as tk    # Import de la librería Tkinter bajo el nombre de "tk"
from tkinter import ttk     # ttk contiene el widget Combobox

# Diccionario de conversiones --definimos un diccionario anidado, con las categorias (subddicionarios) y los valores "base" para cada conversión
conversiones = {
    "Longitud": {
        "Milímetros": 0.001,
        "Centímetros": 0.01,
        "Metros": 1,
        "Kilómetros": 1000
    },
    "Peso": {
        "Gramos": 1,
        "Kilogramos": 1000,
        "Libras": 453.592,
        "Onzas": 28.3495
    },
    "Tiempo": {
        "Segundos": 1,
        "Minutos": 60,
        "Horas": 3600
    },
    "Temperatura": ["Celsius", "Fahrenheit", "Kelvin"] # temperatura es un caso especial, contiene una lista
}

# Ventana principal de la app
ventana_principal = tk.Tk()
ventana_principal.title("Conversor de unidades simple") # Título que se muestra en la ventana principal
ventana_principal.geometry("400x350") # Tamaño: ancho x alto, en píxeles

# Combobox para el tipo de conversión (categorias ejemplo "Longitud...")
tk.Label(ventana_principal, text="Tipo de conversión a realizar: ").pack(pady=5)
combobox_categorias_desplegable = ttk.Combobox(ventana_principal, values=list(conversiones.keys()), state="readonly")
combobox_categorias_desplegable.current(0)
combobox_categorias_desplegable.pack()

# Combobox de unidades origen
tk.Label(ventana_principal, text="De: ").pack(pady=5)
unidad_origen = ttk.Combobox(ventana_principal, state="readonly")
unidad_origen.pack()

# Combobox para unidades de destino
tk.Label(ventana_principal, text="A: ").pack(pady=5)
unidad_destino = ttk.Combobox(ventana_principal, state="readonly")
unidad_destino.pack()

# Campo de entrada
tk.Label(ventana_principal, text="Valor o unidad a convertir: ").pack(pady=5)
entrada = tk.Entry(ventana_principal)
entrada.pack(pady=5)

# Etiqueta dónde se mostrará el resultado
resultado = tk.Label(ventana_principal, text="", font=("Arial", 10, "bold"))
resultado.pack(pady=15)

# Función para atualizar unidades cuando cambia el tipo
def actualizar_unidades(event=None):
    categoria_seleccionada = combobox_categorias_desplegable.get()
    if categoria_seleccionada == "Temperatura":
        unidades = conversiones["Temperatura"]
    else:
        unidades = list(conversiones[categoria_seleccionada].keys())
    unidad_origen.config(values=unidades)
    unidad_destino.config(values=unidades)
    unidad_origen.current(0)
    if len(unidades) > 1:
        unidad_destino.current(1)

combobox_categorias_desplegable.bind("<<ComboboxSelected>>", actualizar_unidades)
actualizar_unidades() # Se llama al inicio para llenar los combos

# Función de conversión
def convertir():
    try:
        valor = float(entrada.get())   # lee el número
        categoria_seleccionada = combobox_categorias_desplegable.get()
        origen = unidad_origen.get()
        destino = unidad_destino.get()
        
        # Conversión estándar (usando los valores base)
        base = conversiones[categoria_seleccionada][origen]
        destino_valor = conversiones[categoria_seleccionada][destino]
        resultado_valor = valor * (base / destino_valor)       

        resultado.config(
            text=f"{valor} {origen} = {resultado_valor:.4f} {destino}"
        )   
    except ValueError:
        resultado.config(text="Ingrese un número válido")

# Funcion conversión para temperaturas
def convertir_temperaturas():
    try:
        valor = float(entrada.get())   # lee el número
        categoria_seleccionada = combobox_categorias_desplegable.get()
        origen = unidad_origen.get()
        destino = unidad_destino.get()

        if categoria_seleccionada == "Temperatura":
            if origen == destino:
                resultado_valor = valor
            elif origen == "Celsius" and destino == "Fahrenheit":
                resultado_valor = (valor * 9/5) + 32
            elif origen == "Fahrenheit" and destino == "Celsius":
                resultado_valor = (valor - 32) * 5/9
            elif origen == "Celsius" and destino == "Kelvin":
                resultado_valor = valor + 273.15
            elif origen == "Kelvin" and destino == "Celsius":
                resultado_valor = valor - 273.15
            elif origen == "Fahrenheit" and destino == "Kelvin":
                resultado_valor = (valor - 32) * 5/9 + 273.15
            elif origen == "Kelvin" and destino == "Fahrenheit":
                resultado_valor = (valor - 273.15) * 9/5 + 32
    except ValueError:
        resultado.config(text="Ingrese un número válido")

# Función intermedia para el botón (así funciona también convertir_temperaturas())
def boton_convertir():
    categoria = combobox_categorias_desplegable.get()
    if categoria == "Temperatura":
        convertir_temperaturas()
    else:
        convertir()

# Botón convertir
boton = tk.Button(ventana_principal, text="Convertir", command=boton_convertir)
boton.pack(pady=10)

# Bucle principal de la app - mantiene la ventana principal abierta
ventana_principal.mainloop()
