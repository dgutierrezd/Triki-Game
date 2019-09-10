#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:53:59 2019

@author: daniel
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:40:55 2019

@author: daniel
"""

from functools import partial
import random
import tkinter as tk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()
middleFrame = tk.Frame(root)
middleFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack()

space1 = tk.Button(topFrame, text='1', height = 10, width = 10, command=lambda: jugadaPlayer(space1, True))
space2 = tk.Button(topFrame, text='2', height = 10, width = 10, command=lambda: jugadaPlayer(space2, True))
space3 = tk.Button(topFrame, text='3', height = 10, width = 10, command=lambda: jugadaPlayer(space3, True))
space4 = tk.Button(middleFrame, text='4', height = 10, width = 10, command=lambda: jugadaPlayer(space4, True))
space5 = tk.Button(middleFrame, text='5', height = 10, width = 10, command=lambda: jugadaPlayer(space5, True))
space6 = tk.Button(middleFrame, text='6', height = 10, width = 10, command=lambda: jugadaPlayer(space6, True))
space7 = tk.Button(bottomFrame, text='7', height = 10, width = 10, command=lambda: jugadaPlayer(space7, True))
space8 = tk.Button(bottomFrame, text='8', height = 10, width = 10, command=lambda: jugadaPlayer(space8, True))
space9 = tk.Button(bottomFrame, text='9', height = 10, width = 10, command=lambda: jugadaPlayer(space9, True))

space1.pack(side=tk.LEFT)
space2.pack(side=tk.LEFT)
space3.pack(side=tk.LEFT)
space4.pack(side=tk.LEFT)
space5.pack(side=tk.LEFT)
space6.pack(side=tk.LEFT)
space7.pack(side=tk.LEFT)
space8.pack(side=tk.LEFT)
space9.pack(side=tk.LEFT)
tk.Label(root, text="Tu eres la letra X, la CPU es la letra O \nEscoge donde quieres hacer tu jugada.").pack()
    
tk.mainloop()
    
def jugadaPlayer(boton, estado):
    verificarEspacios()
    if estado is True:
        boton['text'] = 'X'
        boton['state'] = DISABLED
        verificarEspacios()
        generarNumeroRandom()
    else:
        return boton

def jugadaCPU(boton):    
    verificarEspacios()
    print(boton)
    if boton['text'] is 'X' or boton['text'] is 'O':
        generarNumeroRandom()
        return
    else:
        boton['text'] = 'O'
        boton['state'] = DISABLED
        verificarEspacios()
        
        
def generarNumeroRandom():
    randomNum = random.randint(1,9) 
    
    if randomNum == 1:
        jugadaCPU(space1)
    elif randomNum == 2:
        jugadaCPU(space2)
    elif randomNum == 3:
        jugadaCPU(space3)
    elif randomNum == 4:
        jugadaCPU(space4)
    elif randomNum == 5:
        jugadaCPU(space5)
    elif randomNum == 6:
        jugadaCPU(space6)
    elif randomNum == 7:
        jugadaCPU(space7)
    elif randomNum == 8:
        jugadaCPU(space8)
    elif randomNum == 9:
        jugadaCPU(space9)
        
    return randomNum

def verificarEspacios():
    if space1['text'] is space2['text'] and space2['text'] is space3['text']:
        terminarJuego(space1['text'])
    elif space4['text'] is space5['text'] and space5['text'] is space6['text']:
        terminarJuego(space4['text'])
    elif space7['text'] is space8['text'] and space8['text'] is space9['text']:
        terminarJuego(space7['text'])
    elif space1['text'] is space4['text'] and space4['text'] is space7['text']:
        terminarJuego(space1['text'])
    elif space2['text'] is space5['text'] and space5['text'] is space8['text']:
        terminarJuego(space2['text'])
    elif space3['text'] is space6['text'] and space6['text'] is space9['text']:
        terminarJuego(space3['text'])
    elif space1['text'] is space5['text'] and space5['text'] is space9['text']:
        terminarJuego(space1['text'])
    elif space3['text'] is space5['text'] and space5['text'] is space7['text']:
        terminarJuego(space3['text'])
    else:
        return
        
def terminarJuego(ganador):
    tk.messagebox.showinfo("Fin del juego", f"El juego ha terminado, {ganador} gano!'")
    root.destroy()