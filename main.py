# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

# Builtin
import tkinter as tk

# Módulo próprio
from app.calculadora import Calculadora
# Este es un cambio menor al archivo para hacer una prueba de edición. 
if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    main.start()
