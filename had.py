# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:38:49 2018

@author: Tom-PC
"""


import pyglet, time
from pyglet.window.key import MOD_CTRL, A, B, C, DOWN, UP, LEFT, RIGHT, W, S, D
from random import randrange
from math import cos, sin, pi, radians

zelena = pyglet.image.load("zelena.png")
cervena = pyglet.image.load("cervena.png")
bila = pyglet.image.load("bila.png")


window = pyglet.window.Window(800, 600)
batch = pyglet.graphics.Batch() 
seznam = list()
typhry=3
stary_smer = 0, 1
CTVER = 8   #konstanta pro velikost čtverce


def konec():
    time.sleep(2)   
    window.close()

class Hrac(object):
    def __init__(self):
        self.had = [(50, 6), (60, 6)]       #max hodnota pole x = 99, y = 74
        self.sirka = 30
        self.vyska = 30
        self.jidlo = []
        self.jidlonew() 
        self.smer = 0, 1
        self.vybs= []


    def pohyb(self):
        global stary_smer
        stary_smer = stary_smer
        if self.vybs:
            print(self.vybs)
            novy_smer = self.vybs[0]
            del self.vybs[0]
            old_x, old_y = self.had[-1]
            new_x, new_y = self.smer
            if (old_x, old_y) != (-new_x, -new_y):
                self.smer = novy_smer


        old_x, old_y = self.had[-1]
       
        smer_x, smer_y = self.smer

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
        else:
            del self.had[0]
        
        
        if typhry == 1 or typhry == 2:             #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            if new_x < 2:
                konec()
            if new_y < 2:
                konec()
            if new_x > 97:
                konec()
            if new_y > 72:
                konec()
        if typhry == 2:
            if new_x > 47 and new_x < 52 and new_y > 35 and new_y < 40:
                konec()
        if typhry == 3:
            if new_x < 16 and new_y < 2:
                konec()
            if new_x < 2 and new_y < 12:
                konec()
            if new_x < 2 and new_y > 62:
                konec()
            if new_x < 16 and new_y > 72:
                konec()
            if new_x > 83 and new_y < 2:
                konec()
            if new_x > 97 and new_y < 12:
                konec()
            if new_x > 83 and new_y > 72:
                konec()
            if new_x > 97 and new_y > 62:
                konec()
                       
        
        
    def jidlonew(self):
        for cislo in range(100):
            jx = randrange(2, 81)
            jy = randrange(2, 72)
            jpozice = jx, jy
            if jx and jy not in self.had:
                if typhry == 2:
                    if jx not in range(47, 52) and jy not in range(35, 40):
                        self.jidlo.append(jpozice)
                        return
                else:
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




if typhry == 1 or typhry == 2:
    okrajL = Had(obrazek="bila.png", x=1, y=300, vyska=600, sirka=30)
    okrajP = Had(obrazek="bila.png", x=799, y=300, vyska=600, sirka=30, r=180)
    okrajH = Had(obrazek="bila.png", x=400, y=599, vyska=30, sirka=800)
    okrajD = Had(obrazek="bila.png", x=400, y=1, vyska=30, sirka=800, r=180)
if typhry == 2:
    kostka = Had(obrazek="bila.png", rychlost=100, r=180, x=400, y=303, vyska=33)    
if typhry == 3:
    rohLH = Had(obrazek="bila.png", x=1, y=599, vyska=30, sirka=250)
    rohLH2 = Had(obrazek="bila.png", x=1, y=599, vyska=188, sirka=30)
    rohLD = Had(obrazek="bila.png", x=1, y=1, vyska=30, sirka=250)
    rohLD2 = Had(obrazek="bila.png", x=1, y=1, vyska=188, sirka=30)
    rohPH = Had(obrazek="bila.png", x=799, y=599, vyska=30, sirka=250)
    rohPH2 = Had(obrazek="bila.png", x=799, y=599, vyska=188, sirka=30)
    rohPD = Had(obrazek="bila.png", x=799, y=1, vyska=30, sirka=250)
    rohPD2 = Had(obrazek="bila.png", x=799, y=1, vyska=188, sirka=30)
    
    
@window.event    
def on_mouse_press(x, y, button, mod):
    print(x, y, button, mod)



@window.event
def on_key_press(sym, mod):
    global stary_smer
    try:
        if stary_smer == (0, -1):
            pass
        else:
            if sym == UP or sym == W:
                novy_smer = 0, 1
            
        if stary_smer == (0, 1):
            pass
        else:
            if sym == DOWN or sym == S:
                novy_smer = 0, -1
        
        if stary_smer == (1, 0):
            pass
        else:
            if sym == LEFT or sym == A:
                novy_smer = -1, 0
        
        if stary_smer == (-1, 0):
            pass
        else:
            if sym == RIGHT or sym == D:
                novy_smer = 1, 0
        
        stary_smer = novy_smer
        hrac.vybs.append(novy_smer)
        
        print(sym, mod)
    except:
        pass

def tik(t):
    hrac.pohyb()

pyglet.clock.schedule_interval(tik, 1/30)  

pyglet.app.run()