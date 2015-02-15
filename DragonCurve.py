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

lista = []

def calcola(n):
    if n == 0:
        return 0
    else:
        l = pow(2, math.floor(math.log(n,2))+1) - n - 1
        lista.append((calcola(l) + 1)%4)		
        return (calcola(l) + 1)%4

def creastringa(n):
    stringa = ''
    for i in range(0, n):
        stringa += str(calcola(i))
    print(stringa)

n = input("Quanti numeri vuoi calcolare?\n")
creastringa(n)
print("Cose!")
