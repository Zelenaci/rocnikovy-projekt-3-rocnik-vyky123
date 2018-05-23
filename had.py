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
had = [(1,2)]
jidlo = [(6,8)]
xold = 10
yold = 10
klavesy = set()


def konec():
    time.sleep(2)   
    window.close()

class Hrac(object):
    def __init__(self):
        self.jidlo = []
        self.jidlonew()
        self.jidlonew()
        self.had = [(0, 0), (1, 0)]
        self.sirka = 30
        self.vyska = 30
        self.smer = 0, 1
        self.vybs= []
        
    def pohyb(self):
        novy_smer = self.vybs[0]
        del self.vybs[0]
        old_x, old_y = self.had[-1]
        new_x, new_y = self.smer
        if (old_x, old_y) != (-new_x, -new_y):
            self.smer = novy_smer

        old_x = self.had[-1]
        old_y = self.had[-1]

        smer_x = self.smer
        smer_y = self.smer

        new_x = old_x + smer_x
        new_y = old_y + smer_y

        new_x = new_x % self.width
        new_y = new_y % self.height

        hlava = new_x, new_y
        if hlava in self.had:
            konec
        self.had.append(hlava)

        if hlava in self.jidlo:
            self.jidlo.remove(hlava)
            self.jidlonew()
        else:
            del self.had[0]


    def jidlonew(self):
        jx = randint(50, window.width - 50)
        jy = randint(50, window.height - 50)
        if jx and jy not in self.had:
            self.jidlo.append(jx,jy)
            return


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



    def hranice(self):
        min_x = -self.image.width // 2
        min_y = -self.image.height // 2
        max_x = 800 + self.image.width // 2
        max_y = 600 + self.image.height // 2
        if kostka._x < min_x:
            kostka._x = max_x
        elif kostka._x > max_x:
            kostka._x = min_x
        if kostka._y < min_y:
            kostka._y = max_y
        elif kostka._y > max_y:
           kostka._y = min_y   


    def tik(self, t):
        self.sprite.x = self.sprite.x + self._rychlost*t*sin(pi*self._rotation/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + self._rychlost*t*cos(pi*self._rotation/180)
        self._y = self.sprite.y
        self.hranice()

        if typhry == 1:
            if kostka._x < 21:
                konec
            if kostka._y < 21:
                konec
            if kostka._x > window.width - 21:
                konec
            if kostka._y > window.height - 21:
                konec
        print("s: ",kostka._x,kostka._y)



state = Hrac()
state.width = window.width // CTVER
state.height = window.height // CTVER


   
    
@window.event
def on_draw():
    window.clear()



    for _x, _y in had:
        print(_x,_y)
        zelena.blit(_x * CTVER, _y * CTVER, width=CTVER, height=CTVER)
    for _x, _y in jidlo:
        cervena.blit(_x * CTVER, _y * CTVER, width=CTVER, height=CTVER)
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
kostka = Had(obrazek="zelena.png", rychlost=100, r=180, x=400, y=300)    
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
    Hrac.vybs(novy_smer)
    print(sym, mod)

def pohyb(dt):
    state.move()

pyglet.clock.schedule_interval(pohyb, 1/30)  

pyglet.app.run()