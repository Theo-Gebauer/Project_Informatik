import pgzrun

WIDTH = 1280
HEIGHT = 720

#globale Variablen
MOVE_SPEED = 5
JUMP_SPEED = 20
GRAVITY = 0.7
MAX_FALL_SPEED = 15

#Charakter
hero  = Actor('red_hero_idle_1', anchor=("center", "bottom"))
hero.midbottom = (100, 100)

hero.vx = 0
hero.vy = 0
hero.on_ground = False

#Platformen
platforms = [
    Actor('platform_1', topleft=(100,300)),
    Actor('platform_2', topleft=(500,450)),
    Actor('platform_3', topleft=(1000,350))
]

#Methoden

#Update
def update():
    #vx berechnen
    hero.vx = 0
    if keyboard.left:
        hero.vx = -MOVE_SPEED
    elif keyboard.right:
        hero.vx = MOVE_SPEED

    #vy berechnen
    if keyboard.space and hero.on_ground:
        hero.vy = -JUMP_SPEED

    hero.vy = min(hero.vy + GRAVITY, MAX_FALL_SPEED)

    hero.x += hero.vx

    if hero.vy >= 0:
        target_bottom = hero.y + hero.vy
        
        landing_bottom = HEIGHT

        for platform in platforms:
            if (hero.right > platform.left and hero.left < platform.right and hero.bottom <= platform.top):
                landing_bottom = min(landing_bottom, platform.top)

        if target_bottom >= landing_bottom:
            hero.bottom = landing_bottom
            hero.vy = 0
            hero.on_ground = True
        else:
            hero.bottom = target_bottom
            hero.on_ground = False
    else:
        hero.y += hero.vy
        hero.on_ground = False
    


def draw():
    screen.blit("background",(0,0))
    hero.draw()
    for platform in platforms:
        platform.draw()

pgzrun.go()