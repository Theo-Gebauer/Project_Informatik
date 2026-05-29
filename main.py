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

inventory_player = inventory.Inventory(5,5,42,112)
wave = waves.WaveManager()
inventory_button = Actor('inventory_button', topleft = (10, 10))

def on_mouse_down(button, pos):
    menu.mouse_menu(button, pos)
    if global_var.game_started and not global_var.autoscroll:
        greenhouse.mouse_greenhouse(button,pos)
        alchemy.mouse_alchemy(button, pos)
        inventory_player.mouse(button, pos)
        global_var.mouse_global_var(button)
        if global_var.button_pressed(pos, 30, 30, 30, 30) and button == 1:
            inventory_player.toggle_open()
    #print(pos)

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
        inventory_button.draw()
        if global_var.game_started:
            inventory_player.draw()
    menu.draw_menu()

pgzrun.go()
