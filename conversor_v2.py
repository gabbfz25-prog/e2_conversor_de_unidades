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
ventana_principal.geometry("425x375") # Tamaño: ancho x alto, en píxeles

# Etiqueta "Tipo de conversión..." y Combobox para el tipo de conversión (categorias ejemplo "Longitud...")
#tk.Label(ventana_principal, text="Tipo de conversión a realizar: ", font=("Arial", 10, "bold"), width=30).pack(pady=5) # instancia de la clase Label del módulo de tkinter, NO guardamos en variable, solo mostramos en el Widget de la interfaz con .pack()
tk.Label(
    ventana_principal,
    text="Tipo de conversión a realizar:",
    font=("Arial", 12, "bold"),
    width=30,
    justify="center",
    highlightthickness=1.5,   # grosor del borde
    highlightbackground="gray",  # color del borde
    highlightcolor="blue"   # color del borde al enfocar (opcional)
).pack(pady=10)
combobox_categorias_desplegable = ttk.Combobox(ventana_principal, values=list(conversiones.keys()), state="readonly")
combobox_categorias_desplegable.current(0) # este .current(0) dispara un evento .bind("<<ComboboxSelected>>") al hacer click y elegir la categoría por ej: "Peso"
combobox_categorias_desplegable.pack()

# Etiqueta "De: " y Combobox para las de unidades origen
tk.Label(
    ventana_principal, 
    text="De:",
    font=("Arial", 12, "bold"),
    width=30,
    justify="center",
    ).pack(pady=5)
unidad_origen = ttk.Combobox(ventana_principal, state="readonly")
unidad_origen.pack()

# Combobox para unidades de destino
tk.Label(
    ventana_principal, 
    text="A:",
    font=("Arial", 12, "bold"),
    width=30,
    justify="center",
    ).pack(pady=5)
unidad_destino = ttk.Combobox(ventana_principal, state="readonly")
unidad_destino.pack()

# Campo de entrada
tk.Label(
    ventana_principal,
    text="Valor o unidad a convertir:",
    font=("Arial", 12, "bold"),
    width=30,
    justify="center",
    highlightthickness=1.5,   # grosor del borde
    highlightbackground="gray",  # color del borde
    highlightcolor="blue"   # color del borde al enfocar (opcional)
).pack(pady=10)
entrada = tk.Entry(ventana_principal, font=("Arial", 12, "bold")) # esta es la casilla dónde escribimos el valor con el teclado
entrada.pack(pady=5)
entrada.focus() # Esto hace que al abrir la app, ya esté seleccionado la casilla dónde se capturan los datos por teclado

# Etiqueta dónde se mostrará el resultado
resultado = tk.Label(ventana_principal, text="", font=("Arial", 12, "bold"))
resultado.pack(pady=15)

# Función para atualizar unidades cuando cambia el tipo -----------------------------------------------
def actualizar_unidades(event=None):
    categoria_seleccionada = combobox_categorias_desplegable.get() # obtiene la categería seleccionada para luego hacer las comparaciones 
    if categoria_seleccionada == "Temperatura": 
        unidades = conversiones["Temperatura"] # si la categoría seleccionada es "Temperatura" se almacena en la variable unidades
    else:
        unidades = list(conversiones[categoria_seleccionada].keys())
        unidad_origen.config(values=unidades)
        unidad_destino.config(values=unidades)
        unidad_origen.current(0)
    if len(unidades) > 1:
        unidad_destino.current(1)

combobox_categorias_desplegable.bind("<<ComboboxSelected>>", actualizar_unidades) # En este evento, cada vez que cambie la selección en combobox_categorias_desplegable = ttk.Combobox(), ejecuta la función actualizar_unidades()
actualizar_unidades() # Se llama al inicio para llenar los combos

# Función de conversión
def convertir(event=None):
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

        # Conversión estándar (usando los valores base)
        else:
            base = conversiones[categoria_seleccionada][origen]
            destino_valor = conversiones[categoria_seleccionada][destino]
            resultado_valor = valor * (base / destino_valor)       

        resultado.config(
            text=f"{valor} {origen} = {resultado_valor:.2f} {destino}"
        )   
    except ValueError:
        resultado.config(text="Ingrese un número válido")      

# Botón convertir
# boton = tk.Button(ventana_principal, text="Convertir", command=convertir)
# boton.pack(pady=10)

# Realizar conversión
ventana_principal.bind("<Return>", convertir)

# Bucle principal de la app - mantiene la ventana principal abierta
ventana_principal.mainloop()
