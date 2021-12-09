# -*- coding: utf-8 -*-
"""
@author: NOEMI
"""

def calculadora(o,a,b):
    suma = lambda x,y: x+y
    resta = lambda x,y: x-y
    multiplicacion = lambda x,y: x*y
    division = lambda x,y: x/y
    switcher = {
        "+" : suma(a,b),
        "-" : resta(a,b),
        "*" : multiplicacion(a,b),
        "/" : division(a,b), 
    }
    return switcher.get(o)
    

a = int(input("Primer Numero Entrada: "))
b = int(input("Segundo Numero Entrada: "))
print("Suma:",calculadora("+",a,b))
print("Resta:",calculadora("-",a,b))
print("Multiplicacion:",calculadora("*",a,b))
print("Division:",calculadora("/",a,b))