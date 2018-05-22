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
 #       self.jidlonew()
 #       self.jidlonew()
        self.had = [(0, 0), (1, 0)]
        self.sirka = 30
        self.vyska = 30
        self.smer = 0, 1
        
       
        
        
        
    def pohyb(self):
        old_x, old_y = self.had[-1]
        dir_x, dir_y = self.smer
        
        new_x = old_x + dir_x
        new_y = old_y + dir_y

        new_x = new_x % self.width
        new_y = new_y % self.height

        hlava = new_x, new_y
        if hlava in self.had:
            konec
        self.had.append(hlava)

        if hlava in self.jidlo:
            self.jidlo.remove(hlava)
#            self.jidlonew()
        else:
            del self.had[0]
            
            
#    def jidlonew:
        
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
        
        self.keys = dict(left=False, right=False, up=False)
              
        

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
        #print("x: ",kostka._x)
        #print("y: ",kostka._y)
        if typhry == 1:
            if kostka._x < 21:
                konec
            if kostka._y < 21:
                konec
            if kostka._x > 779:
                konec
            if kostka._y > 579:
                konec
        global xold
        global yold
        xold = kostka._x - 30
        yold = kostka._y - 30
        print("old: ",xold,yold)



    
    
    
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

if typhry ==1:
    okrajL = Had(obrazek="bila.png", x=1, y=300, vyska=600, sirka=20)
    okrajP = Had(obrazek="bila.png", x=799, y=300, vyska=600, sirka=20, r=180)
    okrajH = Had(obrazek="bila.png", x=400, y=599, vyska=20, sirka=800)
    okrajD = Had(obrazek="bila.png", x=400, y=1, vyska=20, sirka=800, r=180)
kostka = Had(obrazek="zelena.png", rychlost=100, r=180, x=400, y=300)
#ocas = Had(obrazek="cervena.png", rychlost=100,r=180 ,x=xold, y=yold, sirka=50,vyska=50)



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
    if sym == UP or sym == W:
        kostka._rotation = 0

    if sym == DOWN or sym == S:
        kostka._rotation = 180
    
    if sym == LEFT or sym == A:
        kostka._rotation = -90
    
    if sym == RIGHT or sym == D:
        kostka._rotation = 90
        
    print(sym, mod)

pyglet.clock.schedule_interval(tik, 1/30)  

pyglet.app.run()