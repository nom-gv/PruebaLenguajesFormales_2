# -*- coding: utf-8 -*-
"""
@author: NOEMI
"""

def calculadora(o,a,b):
    switcher = {
        "+": suma(a,b),
        "-": resta(a,b),
        "*": multiplicacion(a, b),
        "/": division(a,b),
    }     
    return switcher.get(o)
    
    
def suma(x, y):
    return x+y
    
def resta(x, y):
    return x-y
    
def multiplicacion(x, y):
    return x*y
    
def division(x, y):
    return x/y


a = int(input("Primer Numero Entrada: "))
b = int(input("Segundo Numero Entrada: "))
print("Suma:",calculadora("+",a,b))
print("Resta:",calculadora("-",a,b))
print("Multiplicacion:",calculadora("*",a,b))
print("Division:",calculadora("/",a,b))