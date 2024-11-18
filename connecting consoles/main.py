import pgzrun 
import random 

HEIGHT = 600
WIDTH = 800

consoles = []
number_of_consoles = 10
next_console = 0
lines = []

def creating_consoles():
    global console
    for i in range (number_of_consoles):
        console = Actor("console")
        console.pos = (random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))
        consoles.append(console)

def draw():
    screen.clear()
    screen.blit("backround",(0,0))
    for item in consoles:
        item.draw()
    number = 1 
    for item in consoles:
        screen.draw.text(str(number),(item.pos[0],item.pos[1]+20))
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
        

def on_mouse_down(pos):
    global lines,next_console
    if next_console < number_of_consoles:
        if consoles[next_console].collidepoint(pos):
            if next_console:
                lines.append((consoles[next_console-1].pos,consoles[next_console].pos))
            next_console += 1
        else:
            next_console = 0
            lines = []

def update():
    pass 
    


creating_consoles()

pgzrun.go()
