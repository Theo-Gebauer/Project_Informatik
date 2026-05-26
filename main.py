import pgzrun
import random

WIDTH = 1420
HEIGHT = 930 
scroll_y = 0
max_height = HEIGHT - 1680
game_started = False

startbutton = Actor('startknopf', center=(WIDTH//2, HEIGHT//2), anchor=('center', 'center'))

clouds = [
    Actor('cloud1', topleft=(0,max_height+ 10)),
    Actor('cloud2', topleft=(200,max_height+50)),
    Actor('cloud3', topleft=(500,max_height+25)),
    Actor('cloud4', topleft=(500,max_height+60))
]

tower = Actor('turm', midbottom=(WIDTH//2, HEIGHT)) 

background = Actor('hintergrund_tag', bottomright=(WIDTH, HEIGHT), anchor=('left', 'bottom'))

for i in range(4):
    clouds[i].vx = i+1

#Mausabtastung
def on_mouse_down(button,pos):
    global scroll_y
    global game_started

    if not game_started and startbutton.x - 130 < pos[0] < startbutton.x + 130 and startbutton.y - 60 < pos[1] < startbutton.y + 60:
        game_started = True
    else:   
        if button == mouse.WHEEL_UP and background.y < 1680:
            scroll_y = 30
        elif button == mouse.WHEEL_DOWN and background.y > HEIGHT:
            scroll_y = -30


#Update
def update():
    global scroll_y   
    global game_started

    if game_started:
        background.y += scroll_y
        tower.y += scroll_y

        for cloud in clouds:
            if cloud.left <= WIDTH:
                cloud.left += cloud.vx
            else:
                cloud.left = -450
                cloud.vx = random.randint(1,3)
            cloud.y += scroll_y
        scroll_y = 0

#Draw

def draw():
    global game_started

    screen.clear()

    background.draw()

    for i in range(2,4):
        clouds[i].draw()

    tower.draw()

    for i in range(0,2):
        clouds[i].draw()

    if not game_started:
        startbutton.draw()

pgzrun.go()