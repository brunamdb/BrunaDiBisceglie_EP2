# -*- coding: utf-8 -*-
#Bruna Machado Di Bisceglie
"""
Created on Tue Mar 24 09:59:48 2015

@author: Bruna
"""
#importar palavras
text = open("palavras.txt", encoding="utf-8")
listasuja = text.readlines()
lista = []
for i in listasuja:
    limpar = i.strip()
    if limpar != "":
        lista.append(limpar)
#fazer janela
import turtle
janela = turtle.Screen()
janela.bgcolor ("purple")
janela.title("jogo da forca")
lapis = turtle.Turtle()
lapis.speed(20)
lapis.color("green")
lapis.penup()
lapis.setpos(-250,250)
lapis.pendown()
#escrever jogodaforca
#J
lapis.forward(150)
lapis.backward(75)
lapis.right(90)
lapis.forward(100)
i = 0
while i <=180:
    lapis.right(1)
    lapis.forward(1)
    i = i+1
#o
lapis.right(90)
lapis.penup()
lapis.setpos(-90, 100)
lapis.pendown()
lapis.circle(40)
#g
lapis.penup()
lapis.setpos(10, 100)
lapis.pendown()
lapis.circle(40)
lapis.penup()
lapis.setpos(50, 140)
lapis.pendown()
lapis.right(90)
lapis.forward(75)
i = 0
while i<=180:
    lapis.right(1)
    lapis.forward(0.75)
    i = i+1
#o
lapis.right(90)
lapis.penup()
lapis.setpos(110, 100)
lapis.pendown()
lapis.circle(40)
#d
lapis.penup()
lapis.setpos(100, 50)
lapis.pendown()
lapis.right(90)
lapis.forward(100)
lapis.left(90)
i=0
while i <=180:
    lapis.left(1)
    lapis.forward(0.9)
    i= i+1
#a
lapis.penup()
lapis.setpos(165,-50)
lapis.right(110)
lapis.pendown()
lapis.forward(100)
lapis.right(130)
lapis.forward(100)
lapis.backward(40)
lapis.right(120)
lapis.forward(50)
#f
lapis.penup()
lapis.setpos(-250,-250)
lapis.pendown()
lapis.right(90)
lapis.forward(150)
lapis.right(90)
lapis.forward(75)
lapis.left(180)
lapis.forward(75)
lapis.left(90)
lapis.forward(75)
lapis.left(90)
lapis.forward(50)
#o
lapis.penup()
lapis.setpos(-125,-250)
lapis.pendown()
lapis.circle(40)
#r
lapis.penup()
lapis.setpos(-50,-250)
lapis.pendown()
lapis.left(90)
lapis.forward(80)
lapis.right(90)
i = 0
while i <=180:
    lapis.forward(0.40)
    lapis.right(1)
    i= i+1
lapis.left(135)
lapis.forward(50)
#c
lapis.penup()
lapis.setpos(50,-250)
lapis.pendown()
lapis.right(135)
i = 0
while i <= 180:
    lapis.forward(0.75)
    lapis.right(1)
    i = i +1
#a
lapis.penup()
lapis.setpos(65,-250)
lapis.left(75)
lapis.pendown()
lapis.forward(90)
lapis.right(140)
lapis.forward(90)
lapis.backward(40)
lapis.right(110)
lapis.forward(40)
#limpar a tela
import time
time.sleep(3)
lapis.clear()


def DesenharForca ():
    lapis.penup()
    lapis.setpos(-250, -250)
    lapis.pendown()
    lapis.right(92)
    lapis.forward(500)
    lapis.right(90)
    lapis.forward(150)
    lapis.right(90)
    lapis.forward(100)

#BONECO
def Cabeça ():
    lapis.penup()
    lapis.setpos(-100, 70)
    lapis.pendown()
    lapis.circle(40)
    
def Corpo ():
    lapis.left(90)
    lapis.penup()
    lapis.setpos(-100, 70)
    lapis.pendown()
    lapis.backward(100)
    lapis.right(90)

def Braço1 ():
    lapis.penup()
    lapis.setpos(-100, 40)
    lapis.pendown()
    lapis.left(135)
    lapis.forward(50)
    lapis.right(135)

def Braço2 ():
    lapis.penup()
    lapis.setpos(-100, 40)
    lapis.pendown()
    lapis.left(45)
    lapis.forward(50)
    lapis.right(45)

def Perna1 ():
    lapis.penup()
    lapis.setpos(-100, -30)
    lapis.pendown()
    lapis.left(135)
    lapis.forward(50)
    lapis.right(135)

def Perna2 ():
    lapis.penup()
    lapis.setpos(-100, -30)
    lapis.pendown()
    lapis.right(135)
    lapis.forward(50)
    lapis.left(135)
    
def ColocandoNoLugarParaTracinho ():
    lapis.penup()
    lapis.setpos(-200, -250)
    lapis.left(90)
    lapis.pendown()

def TracinhoDaLetra():
    lapis.forward(10)
    lapis.penup()
    lapis.forward(10)
    lapis.pendown()
#fazer tracinhos de acordo com tamanho da palavra
def Tracinho(palavra):
    for c in palavra:
        if c == " ":
            lapis.penup()
            lapis.forward(20)
            lapis.pendown()
        else:
            TracinhoDaLetra()
boneco = 0
while lista != [] and boneco < 6:
    #escolher palavra da lista
    lapis.clear()
    DesenharForca()
    ColocandoNoLugarParaTracinho()
    
    from random import choice
    palavra = choice (lista)
    print (palavra)
    lista = lista.remove(palavra)
    Tracinho(palavra)
    letras = []
    boneco = 0
    qt = 0
    if " "in palavra:
        tamanho = len(palavra) -1
    else:
        tamanho = len(palavra)
    while boneco <= 6 and qt < tamanho:
        lapis.penup()
        lapis.setpos(-200, -250)
        lapis.pendown()
        letra = janela.textinput("Inserir Letra", "Insira uma letra")
        while letra in letras:
            letra = janela.textinput("Inserir Letra", "Essa letra já foi, escolha outra:")
        letras.append(letra)
        if letra in palavra or (letra == "a" and palavra.find("ã") != -1) or (letra == "e" and palavra.find("E") != -1) or (letra == "i"and palavra.find("í") != -1) or (letra == "o" and palavra.find("ô") != -1) or (letra == "o" and palavra.find("ó") != -1) or (letra == "b" and palavra.find("B") != -1) or (letra == "s" and palavra.find("S") != -1) or (letra == "p" and palavra.find("P") != -1):
            if letra in palavra:
                caso1 = 0
                ir = 1
                while ir > 0:
                    nletras = len(palavra) 
                    voltar = nletras*20
                    ir = (palavra.find(letra, caso1))*20
                    if ir > 0:
                        caso1 = palavra.find(letra, caso1) +1
                        lapis.penup()
                        lapis.forward(ir)
                        lapis.write(letra, font = ("Arial", 20))
                        lapis.penup()
                        lapis.backward(ir)
                        qt = qt +1
            if letra == "a":
                if palavra.find("ã") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("ã", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("ã", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("ã", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "a":
                if palavra.find("A") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("A", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("A", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("A", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "e":
                if palavra.find("E") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("E", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("E", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("E", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "i":
                if palavra.find("í") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("í", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("í", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("í", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "o":
                if palavra.find("ô") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("ô", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("ô", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("ô", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
                if palavra.find("ó") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("ó", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("ó", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("ó", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "b":
                if palavra.find("B") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("B", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("B", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("B", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "c":
                if palavra.find("C") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("C", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("C", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("C", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "s":
                if palavra.find("S") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("S", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("S", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("S", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            if letra == "p":
                if palavra.find("P") != -1:
                    caso1 = 0
                    ir = 1
                    while ir > 0:
                        nletras = len(palavra) 
                        voltar = nletras*20
                        ir = (palavra.find("P", caso1))*20
                        if ir > 0:
                            caso1 = palavra.find("P", caso1) +1
                            lapis.penup()
                            lapis.forward(ir)
                            lapis.write("P", font = ("Arial", 20))
                            lapis.penup()
                            lapis.backward(ir)
                            qt = qt +1
            
        elif boneco == 0:
            Cabeça()
            boneco = 1
        elif boneco ==1:
            Corpo()
            boneco =2
        elif boneco==2:
            Braço1()
            boneco = 3
        elif boneco == 3:
            Braço2()
            boneco = 4
        elif boneco == 4:
            Perna1 ()
            boneco = 5
        elif boneco == 5:
            Perna2 ()
            boneco = 6
            lapis.clear()
            lapis.penup()
            lapis.setpos(-250, 0)
            lapis.write("Fim do jogo", font = ("Arial", 100))

lapis.write("Você ganhou!", font = ("Arial", 100))
#            
            
        




janela.exitonclick()