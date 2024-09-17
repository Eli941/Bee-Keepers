import pgzrun
from random import randint 

TITLE = "Bee Keeping"
WIDTH = 500
HEIGHT = 500

bee = Actor("bee")
flower = Actor("flower")

bee.pos = (100,100)
flower.pos = (200,200)

def draw():
    screen.clear()
    screen.blit("greenfield",(0,0))
    
    bee.draw()
    flower.draw()


pgzrun.go()