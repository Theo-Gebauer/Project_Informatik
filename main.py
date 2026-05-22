import pgzrun

WIDTH = 1280
HEIGHT = 720

cloud = Actor("cloud1")
cloud.vx = 1
cloud.pos = (0,200)

#Update
def update():
    if cloud.left <= WIDTH:
        cloud.left += cloud.vx
    else:
        cloud.left = -300
        

   
    


def draw():
    screen.blit("backgroundcolorforest",(0,0))
    cloud.draw()
pgzrun.go()