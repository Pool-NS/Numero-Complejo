import tkinter as tk
from tkinter import messagebox
import re


def parsear_numero_complejo(entrada):
    patron = re.compile(r'^([-+]?\d*\.?\d*)?([-+]\d*\.?\d*)i$')
    coincidencia = patron.match(entrada)
    if not coincidencia:
        raise ValueError("Formato no válido. Usa el formato 'a+bi' o 'a-bi'.")

    parte_real = coincidencia.group(1)
    parte_imaginaria = coincidencia.group(2)

    if parte_real == '' or parte_real == '+':
        parte_real = '0'
    if parte_imaginaria == '' or parte_imaginaria == '+':
        parte_imaginaria = '1'
    elif parte_imaginaria == '-':
        parte_imaginaria = '-1'

    return complex(float(parte_real), float(parte_imaginaria))


def realizar_operacion(opcion):
    try:
        numero1 = parsear_numero_complejo(entrada1.get())
        numero2 = parsear_numero_complejo(entrada2.get())

        if opcion == "sumar":
            resultado = numero1 + numero2
        elif opcion == "restar":
            resultado = numero1 - numero2
        elif opcion == "multiplicar":
            resultado = numero1 * numero2
        elif opcion == "dividir":
            resultado = numero1 / numero2
        else:
            raise ValueError("Operación no válida.")

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida.")


# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Números Complejos")

# Configuración de colores y fuentes
root.config(bg='#f0f0f0')

# Etiquetas y campos de entrada
tk.Label(root, text="Número complejo 1:", bg='#f0f0f0').grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(root, text="Número complejo 2:", bg='#f0f0f0').grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entrada1 = tk.Entry(root, width=30)
entrada2 = tk.Entry(root, width=30)

entrada1.grid(row=0, column=1, padx=10, pady=10)
entrada2.grid(row=1, column=1, padx=10, pady=10)

# Botones para operaciones
tk.Button(root, text="Sumar", command=lambda: realizar_operacion("sumar")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Restar", command=lambda: realizar_operacion("restar")).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiplicar", command=lambda: realizar_operacion("multiplicar")).grid(row=3, column=0, padx=10,
                                                                                            pady=10)
tk.Button(root, text="Dividir", command=lambda: realizar_operacion("dividir")).grid(row=3, column=1, padx=10, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado:", bg='#f0f0f0', font=('Arial', 12))
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
