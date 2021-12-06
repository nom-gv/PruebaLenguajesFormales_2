# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:44:00 2021

@author: NOEMI
"""

def calculadora():
    a = int(input("Primer Numero Entrada: "))
    b = int(input("Segundo Numero Entrada: "))
    
    suma = lambda x,y: x+y
    print("Suma:", suma(a,b))
    
    resta = lambda x,y: x-y
    print("Resta:",resta(a,b))
    
    multiplicacion = lambda x,y: x*y
    print("Multiplicacion:",multiplicacion(a,b))
    
    division=lambda x,y: x/y
    print("Division:",division(a,b))
    
calculadora()