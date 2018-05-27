# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:38:49 2018

@author: Tom-PC
"""


import pyglet, time
from pyglet.window.key import MOD_CTRL, A, B, C, DOWN, UP, LEFT, RIGHT, W, S, D
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
typhry=1


CTVER = 8   #konstanta pro velikost čtverce


def konec():
    time.sleep(2)   
    window.close()

class Hrac(object):
    def __init__(self):
        self.had = [(50, 6), (60, 6)]
        self.jidlo = []
        self.jidlonew()
        
        self.sirka = 30
        self.vyska = 30
        self.smer1 = 0
        self.smer2 = 1
        self.vybs= []


    def pohyb(self):
        if self.vybs:
            print(self.vybs)
            novy_smer = self.vybs[0]
            del self.vybs[0]
            old_x, old_y = self.had[-1]
            new_x = self.smer1
            new_y = self.smer2
            if (old_x, old_y) != (-new_x, -new_y):
                self.smer = novy_smer


        old_x, old_y = self.had[-1]
       
        smer_x = self.smer1
        smer_y = self.smer2

        new_x = old_x + smer_x
        new_y = old_y + smer_y

        new_x = new_x % self.width
        new_y = new_y % self.height

        hlava = new_x, new_y
        if hlava in self.had:
            konec()
        self.had.append(hlava)

        if hlava in self.jidlo:
            self.jidlo.remove(hlava)
            self.jidlonew()
     #   else:
     #       del self.had[0]
        
        if typhry == 0:             #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if new_x < 0:
                konec()
            if new_y < 70:
                konec()
            if new_x > window.width - 21:
                konec()
            if new_y > window.height - 21:
                konec()
        
            
            
    def jidlonew(self):
        jx = randint(50, window.width - 50)
        jy = randint(50, window.height - 50)
        jpozice = jx, jy
        if jx and jy not in self.had:
            self.jidlo.append(jpozice)
            return
        
hrac = Hrac()
hrac.width = window.width // CTVER
hrac.height = window.height // CTVER        
      
class Had(object): 
    def __init__(self, obrazek, x=400, y=300, r=None, rychlost=0, sirka=30, vyska=30,
                 window=window, batch=batch):
        self.image = pyglet.image.load(obrazek)
        self.image.width = sirka
        self.image.height = vyska
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        self._x = self.sprite.x = x 
        self._y = self.sprite.y = y

        if r:
            self._rotation = r
        else:
            self._rotation = 0
        self.sprite.rotation = self._rotation

        self._rychlost = rychlost
        seznam.append(self)




    def tik(self, t):
        self.sprite.x = self.sprite.x + self._rychlost*t*sin(pi*self._rotation/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + self._rychlost*t*cos(pi*self._rotation/180)
        self._y = self.sprite.y
        self.hranice()

        if typhry == 1:
            if kostka._x < 21:
                konec()
            if kostka._y < 21:
                konec()
            if kostka._x > window.width - 21:
                konec()
            if kostka._y > window.height - 21:
                konec()
        print("s: ",kostka._x,kostka._y)






   
    
@window.event
def on_draw():
    window.clear()
    batch.draw()


    for _x, _y in hrac.had:
        print(_x,_y)
        zelena.blit(_x * CTVER, _y * CTVER, width=CTVER, height=CTVER)
    for jx, jy in hrac.jidlo:
        cervena.blit(jx * CTVER, jy * CTVER, width=CTVER, height=CTVER)
    #    zelena.blit(400 - CTVER, 300 - CTVER, width=CTVER*4, height=CTVER)  # -CTVER/2 slouží k tomu, aby čtverec byl uprostřed
#
 #   for x, y in jidlo:
  #      cervena.blit(random.randint(3 + CTVER*2, 797 - CTVER*2), random.randint(3 + CTVER, 597 - CTVER*2), width=CTVER, height=CTVER)
#




if typhry ==1:
    okrajL = Had(obrazek="bila.png", x=1, y=300, vyska=600, sirka=20)
    okrajP = Had(obrazek="bila.png", x=799, y=300, vyska=600, sirka=20, r=180)
    okrajH = Had(obrazek="bila.png", x=400, y=599, vyska=20, sirka=800)
    okrajD = Had(obrazek="bila.png", x=400, y=1, vyska=20, sirka=800, r=180)
kostka = Had(obrazek="bila.png", rychlost=100, r=180, x=400, y=300)    
#ocas = Had(obrazek="cervena.png", rychlost=100,r=180 ,x=xold, y=yold, sirka=50,vyska=50)


"""
def tik(t):
    for had in seznam:
        had.tik(t)
"""       

@window.event    
def on_mouse_press(x, y, button, mod):
    print(x, y, button, mod)


print(kostka._x, kostka._y)


@window.event
def on_key_press(sym, mod):
    if sym == UP or sym == W:
        novy_smer = 0, 1

    if sym == DOWN or sym == S:
        novy_smer = 0, -1


    if sym == LEFT or sym == A:
        novy_smer = -1, 0

    if sym == RIGHT or sym == D:
        novy_smer = 1, 0
    hrac.vybs.append(novy_smer)
    print(sym, mod)


def pohyb(t):
    hrac.pohyb()

pyglet.clock.schedule_interval(pohyb, 1/2)  

pyglet.app.run()