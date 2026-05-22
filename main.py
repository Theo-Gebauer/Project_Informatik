import pgzrun
import random
import hintergrund

WIDTH = 1280
HEIGHT = 720

#cloud = Actor("cloud1")
#cloud.vx = 1
#cloud.pos = (0,200)

clouds = [
    Actor('cloud1', topleft=(0,0)),
    Actor('cloud2', topleft=(200,50)),
    Actor('cloud3', topleft=(500,25))
]

for i in range(3):
    clouds[i].vx = i+1



#Update
def update():
    for cloud in clouds:
        if cloud.left <= WIDTH:
            cloud.left += cloud.vx
        else:
            cloud.left = -300
            cloud.vx = random.randint(1,3)


   
    


def draw():
    screen.blit("HintergrundTag",(0,0))
    for cloud in clouds:
        cloud.draw()
pgzrun.go()