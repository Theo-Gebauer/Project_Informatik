import pgzrun
import global_var
import menu
import tower
import greenhouse
import alchemie
import inventory
import monster

WIDTH = 1420
HEIGHT = 930 

def on_mouse_down(button, pos):
    menu.mouse_menu(button, pos)
    if global_var.game_started and not global_var.autoscroll:
        tower.mouse_tower(button, pos)
        greenhouse.mouse_greenhouse(button,pos)
    print(pos)

def update():
    tower.update_tower()
    menu.update_menu()

def draw():
    if global_var.scene == 1:
        tower.draw_tower()
    elif global_var.scene == 2:
        greenhouse.draw_greenhouse()
    elif global_var.scene == 3:
        alchemie.draw_alchemie()
    menu.draw_menu()

pgzrun.go()
