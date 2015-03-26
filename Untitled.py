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
lapis.color("black")
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
    lapis.right(90)
    lapis.circle(40)
    lapis.left(90)
    
def Corpo ():
    lapis.penup()
    lapis.forward(80)
    lapis.pendown()
    lapis.forward(100)
    lapis.backward(70)

def Braço1 ():
    lapis.left(45)
    lapis.forward(50)

def Braço2 ():
    lapis.backward(50)
    lapis.right(90)
    lapis.forward(50)

def Perna1 ():
    lapis.backward(50)
    lapis.left(45)
    lapis.forward(70)
    lapis.left(45)
    lapis.forward(50)

def Perna2 ():
    lapis.backward(50)
    lapis.right(90)
    lapis.forward(50)
    lapis.right(135)
    
def ColocandoNoLugarParaTracinho ():
    lapis.penup()
    lapis.setpos(-200, -250)

def TracinhoDaLetra():
    lapis.forward(20)
    lapis.penup()
    lapis.forward(10)
    lapis.pendown()

jogar = "sim"
while jogar == "sim":
    #escolher palavra da lista
    DesenharForca()
    from random import choice
    palavra = choice (lista)
    lista = lista.remove(palavra)
    #fazer tracinhos de acordo com tamanho da palavra
    def Tracinho(palavra):
        for c in palavra:
            if c == " ":
                lapis.penup()
                lapis.forward(30)
                lapis.pendown()
            else:
                TracinhoDaLetra()
    Tracinho (palavra)
    import window
    letra = window.textinput("Inserir Letra", "Insira uma letra")
    if letra in palavra:
        palavra.find(letra)
        

janela.exitonclick()