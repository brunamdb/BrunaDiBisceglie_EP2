# -*- coding: utf-8 -*-
#Bruna Machado Di Bisceglie
"""
Created on Tue Mar 24 09:59:48 2015

@author: Bruna
"""

text = open("palavras.txt", encoding="utf-8")
lista = text.readlines()
limpa = []
for i in lista:
    limpar = i.strip()
    if limpar != "":
        limpa.append(limpar)
print (limpa)
