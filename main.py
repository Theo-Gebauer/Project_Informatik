import pgzrun
import global_var
import menu
import tower
import greenhouse
import alchemy
import inventory
import greenhouse
import items

WIDTH = 1420
HEIGHT = 930 

inventory_button = Actor('inventory_button', topleft = (10, 10))


def on_mouse_down(button, pos):
    menu.mouse_menu(button, pos)
    if global_var.game_started and not global_var.autoscroll:

        if global_var.scene == 1:
            tower.mouse_tower(button, pos)
        elif global_var.scene == 2:
            greenhouse.mouse_greenhouse(button,pos)
        elif global_var.scene == 3:
            alchemy.mouse_alchemy(button, pos)

        global_var.mouse_global_var(button, pos)
    #print(pos)
    #print(global_var.absolutey)

def update():
    tower.update_tower()
    menu.update_menu()

    if global_var.game_started:
        greenhouse.update_greenhouse()

    global_var.update_global_var()
    

def draw():
    if global_var.scene == 1:
        tower.draw_tower(screen)
    elif global_var.scene == 2:
        greenhouse.draw_greenhouse(screen)
    elif global_var.scene == 3:
        alchemy.draw_alchemy(screen)

    if global_var.game_started:
        inventory_button.draw()
    menu.draw_menu()
    global_var.draw(screen)

pgzrun.go()
