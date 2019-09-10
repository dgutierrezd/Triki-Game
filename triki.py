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

def graphicTriki(estado):
    space1 = tk.Button(topFrame, text='1', height = 10, width = 10, command=lambda: jugadaPlayer(space1, True))
    space2 = tk.Button(topFrame, text='2', height = 10, width = 10, command=lambda: jugadaPlayer(space2, True))
    space3 = tk.Button(topFrame, text='3', height = 10, width = 10, command=lambda: jugadaPlayer(space3, True))
    space4 = tk.Button(middleFrame, text='4', height = 10, width = 10, command=lambda: jugadaPlayer(space4, True))
    space5 = tk.Button(middleFrame, text='5', height = 10, width = 10, command=lambda: jugadaPlayer(space5, True))
    space6 = tk.Button(middleFrame, text='6', height = 10, width = 10, command=lambda: jugadaPlayer(space6, True))
    space7 = tk.Button(bottomFrame, text='7', height = 10, width = 10, command=lambda: jugadaPlayer(space7, True))
    space8 = tk.Button(bottomFrame, text='8', height = 10, width = 10, command=lambda: jugadaPlayer(space8, True))
    space9 = tk.Button(bottomFrame, text='9', height = 10, width = 10, command=lambda: jugadaPlayer(space9, True))
    
    #label1.pack(side=tk.LEFT)
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
    
    
def jugadaPlayer(boton, estado):
    if estado is True:
        boton['text'] = 'X'
        boton['state'] = DISABLED
        jugadaCPU()
    else:
        return boton

def jugadaCPU():
    buttons = {}
    
    randomNum = random.randint(1,9)
    #boton = f'space{randomNum}'
    space = 'El boton'
    buttons[space] = f'space{randomNum}'
    boton = buttons[space]
    print(boton[state])
    
    #if boton['state'] == DISABLED:
     #   jugadaCPU()
    #else:
     #   boton['text'] = 'O'
      #  boton['state'] = DISABLED
        

graphicTriki(False)
tk.mainloop()