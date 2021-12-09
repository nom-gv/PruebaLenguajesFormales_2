# -*- coding: utf-8 -*-
"""
@author: NOEMI
"""

def calculadora(funcion, a, b):
    funcion(a,b)
    
def suma(x, y):
    print("Suma:",x+y)   
def resta(x, y):
    print("Resta:",x-y)   
def multiplicacion(x, y):
    print("Multiplicacion",x*y)   
def division(x, y):
    print("Division:",x/y)


a = int(input("Primer Numero Entrada: "))
b = int(input("Segundo Numero Entrada: "))
calculadora(suma,a,b)
calculadora(resta,a,b)
calculadora(multiplicacion,a,b)
calculadora(division,a,b)