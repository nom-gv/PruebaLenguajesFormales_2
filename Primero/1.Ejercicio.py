# -*- coding: utf-8 -*-
"""
@author: NOEMI
"""

def calculadora(s, r, m, d):
    a = int(input("Primer Numero Entrada: "))
    b = int(input("Segundo Numero Entrada: "))
    s(a, b)
    r(a, b)
    m(a, b)
    d(a, b)
    
    
def suma(x, y):
    print("Suma:",x+y)
    
def resta(x, y):
    print("Resta:",x-y)
    
def multiplicacion(x, y):
    print("Multiplicacion",x*y)
    
def division(x, y):
    print("Division:",x/y)

calculadora(suma, resta, multiplicacion, division)