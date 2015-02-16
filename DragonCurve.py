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
img = Image.new( 'RGB', (1300,650), "white") # create a new white image
draw = ImageDraw.Draw(img)

def compute(n):
    if n == 0:
        return 0
    else:
        l = pow(2, math.floor(math.log(n,2))+1) - n - 1	
        return (compute(l) + 1)%4
        #Recursive function to calculate a single number in the series.

def createstring(n):
    string = ''
    for i in range(0, n):
        string += str(compute(i))
        #Create the string 01212321...
    return string

def line(x, y, length, width, direction):
    if direction == 0:
        for i in range(x-length, x, 1):
            for j in range(y, y+width, 1):
                pixels[i,j] = (100, 100, 100)
    elif direction == 1:
        for i in range(x, x+width, 1):
            for j in range(y, y+length+1, 1):
                pixels[i,j] = (100, 100, 100)
    elif direction == 2:
        for i in range(x, x+length+1, 1):
            for j in range(y, y+width, 1):
                pixels[i,j] = (100, 100, 100)
    elif direction == 3:
        for i in range(x, x+width, 1):
            for j in range(y-length, y, 1):
                pixels[i,j] = (100, 100, 100)
    else:
        print("Invalid direction!")


n = int(input("How many lines do you want?\n"))
string = createstring(n)

pixels = img.load() # create the pixel map
x = img.size[0] / 2 # start at the center
y = img.size[1] / 2

while n > 0:
    length = 5
    width = 1
    k = int(string[n-1])
    line(x, y, length, width, k)
    if k == 0:
        x -= length
    elif k == 1:
        y += length
    elif k == 2:
        x += length
    elif k == 3:
        y -= length
    n = n-1
    #Cycle to draw n lines

img.show("out.png", "PNG")
img.save("out.png", "PNG")
