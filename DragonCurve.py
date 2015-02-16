#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DragonCurve.py
#  
#  Copyright 2014 jacopo <jacopo@vikingmetal>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import math
import Image, ImageDraw
from random import randint as rint
img = Image.new( 'RGB', (255,255), "black")
draw = ImageDraw.Draw(img)

def calcola(n):
    if n == 0:
        return 0
    else:
        l = pow(2, math.floor(math.log(n,2))+1) - n - 1	
        return (calcola(l) + 1)%4
        #Recursive function to calculate a single number in the series.

def creastringa(n):
    stringa = ''
    for i in range(0, n):
        stringa += str(calcola(i))
        #Create the string 01212321...

n = input("Quanti numeri vuoi calcolare?\n")
creastringa(n)


img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map


x = img.size[0] / 2
y = img.size[1] / 2

for i in range(x, x+5):    # for every pixel:
    for j in range(y):
        pixels[i,j] = (i, j, 100) # set the colour accordingly


print(x)
print(y)
#draw.line((x, x+5, y, y), fill=rgb(255,0,0))


img.save("out.png", "PNG")
