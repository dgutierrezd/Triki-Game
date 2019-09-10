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

from tkinter import *

def graphic():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()
    middleFrame = Frame(root)
    middleFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack()
    
    space1 = Button(topFrame, text='1', height = 10, width = 10)
    space2 = Button(topFrame, text='2', height = 10, width = 10)
    space3 = Button(topFrame, text='3', height = 10, width = 10)
    space4 = Button(middleFrame, text='4', height = 10, width = 10)
    space5 = Button(middleFrame, text='5', height = 10, width = 10)
    space6 = Button(middleFrame, text='6', height = 10, width = 10)
    space7 = Button(bottomFrame, text='7', height = 10, width = 10)
    space8 = Button(bottomFrame, text='8', height = 10, width = 10)
    space9 = Button(bottomFrame, text='9', height = 10, width = 10)
    
    space1.pack(side=LEFT)
    space2.pack(side=LEFT)
    space3.pack(side=LEFT)
    space4.pack(side=LEFT)
    space5.pack(side=LEFT)
    space6.pack(side=LEFT)
    space7.pack(side=LEFT)
    space8.pack(side=LEFT)
    space9.pack(side=LEFT)
    
    root.mainloop()
    
graphic()