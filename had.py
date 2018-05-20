# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:38:49 2018

@author: Tom-PC
"""


import pyglet
from pyglet.window.key import MOD_CTRL, A, B, C, DOWN, UP, LEFT, RIGHT, S
from pyglet.window.mouse import LEFT as mLEFT
from pyglet.window.mouse import RIGHT as mRIGHT
from random import randint
from math import cos, sin, pi, radians

zelena = pyglet.image.load("zelena.png")
cervena = pyglet.image.load("cervena.png")
bila = pyglet.image.load("bila.png")


window = pyglet.window.Window(800, 600)
batch = pyglet.graphics.Batch() 
seznam = list()



CTVER = 8   #konstanta pro velikost čtverce
had = [(1,2)]
jidlo = [(6,8)]

rychlost = 10
klavesy = set()


class Had(object): 
    def __init__(self, obrazek, x=None, y=None, r=None, rychlost=10,
                 window=window, batch=batch):
        self.image = pyglet.image.load("bila.png")
        self.image.width = 30
        self.image.height = 30
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        
        self._x = self.sprite.x = x 
        self._y = self.sprite.y = y
        
        if r:
            self._rotation = r
        else:
            self._rotation = 90
        self.sprite.rotation = self._rotation
        
        self._rychlost = rychlost
        seznam.append(self)
        
    def hranice(self):
        min_x = -self.image.width // 2
        min_y = -self.image.height // 2
        max_x = 800 + self.image.width // 2
        max_y = 600 + self.image.height // 2
        if self._x < min_x:
            self._x = max_x
        elif self._x > max_x:
            self._x = min_x
        if self._y < min_y:
            self._y = max_y
        elif self._y > max_y:
            self._y = min_y
   

    def tik(self, t):
        self.sprite.x = self.sprite.x + self._rychlost*t*sin(pi*self._rotation/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + self._rychlost*t*cos(pi*self._rotation/180)
        self._y = self.sprite.y
        self.hranice()
        print("x: ",self._x)
        print("y: ",self._y)


    
        

    

@window.event
def on_draw():
    window.clear()
    batch.draw()
   # for x, y in had:
    #    zelena.blit(400 - CTVER, 300 - CTVER, width=CTVER*4, height=CTVER)  # -CTVER/2 slouží k tomu, aby čtverec byl uprostřed
#
 #   for x, y in jidlo:
  #      cervena.blit(random.randint(3 + CTVER*2, 797 - CTVER*2), random.randint(3 + CTVER, 597 - CTVER*2), width=CTVER, height=CTVER)
#


kostka = Had("bila.png", rychlost=30, r=180, x=400, y=300)


def tik(t):
    for had in seznam:
        had.tik(t)
       

@window.event    
def on_mouse_press(x, y, button, mod):
    print(x, y, button, mod)


print(kostka._x, kostka._y)



@window.event
def on_key_press(sym, mod):
    global klavesy
    klavesy.add(sym)
    
    global uhel
    global rychlost
    if sym == 65362:
        uhel = 0
        kostka.sprite.r = 0
    
    elif sym == 65363:
        uhel = 90
        kostka.sprite.r = 90
    
    elif sym == 65364:
        uhel = 180
        kostka.sprite.r = 180
    
    elif sym == 65361:
        uhel = 270
        kostka.sprite.r = -90
 
    print(sym, mod)

pyglet.clock.schedule_interval(tik, 1/30)  

pyglet.app.run()