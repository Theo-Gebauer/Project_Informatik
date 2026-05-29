import pgzrun
import global_var
import menu
import tower
import greenhouse
import alchemy
import inventory
import waves

WIDTH = 1420
HEIGHT = 930 

wave = waves.WaveManager()

def on_mouse_down(button, pos):
    menu.mouse_menu(button, pos)
    if global_var.game_started and not global_var.autoscroll:
        greenhouse.mouse_greenhouse(button,pos)
        alchemy.mouse_alchemy(button, pos)
        inventory.mouse_inventory(button, pos)
        global_var.mouse_global_var(button)
    print(pos)
    print(global_var.absolutex)
    print(global_var.absolutey)

def update():
    tower.update_tower()
    menu.update_menu()
    if global_var.game_started:
        wave.update()
    global_var.update_global_var()

def draw():
    if global_var.scene == 1:
        tower.draw_tower()
        if global_var.game_started:
            wave.draw()
    elif global_var.scene == 2:
        greenhouse.draw_greenhouse()
    elif global_var.scene == 3:
        alchemy.draw_alchemy()
    if global_var.game_started:
        if global_var.game_started:
            inventory.draw_inventory()
    menu.draw_menu()

pgzrun.go()
