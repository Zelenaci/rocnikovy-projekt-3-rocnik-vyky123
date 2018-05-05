# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:38:49 2018

@author: Tom-PC
"""

import pyglet, random

zelena = pyglet.image.load("zelena.png")
cervena = pyglet.image.load("cervena.png")
bila = pyglet.image.load("bila.png")

CTVER = 8   #konstanta pro velikost čtverce
had = [(1,2)]
jidlo = [(6,8)]


window = pyglet.window.Window(800, 600)

@window.event
def on_draw():
    window.clear()
    for x, y in had:
        zelena.blit(400 - CTVER, 300 - CTVER, width=CTVER*4, height=CTVER)  # -CTVER/2 slouží k tomu, aby čtverec byl uprostřed

    for x, y in jidlo:
        cervena.blit(random.randint(3 + CTVER*2, 797 - CTVER*2), random.randint(3 + CTVER, 597 - CTVER*2), width=CTVER, height=CTVER)


@window.event    
def on_mouse_press(x, y, button, mod):
    print(x, y, button, mod)


pyglet.app.run()