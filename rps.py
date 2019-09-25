import arcade
import random

WIDTH =  1365
HEIGHT = 710

current_screen = "menu"

x = 0
y = 0
xx = 0


def update(delta_time):
    pass



def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()


def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "menu":
        menu_keybinds(key, modifiers)
    elif current_screen == "instructions":
        instructions_keybinds(key, modifiers)
    elif current_screen == "play":
        play_keybinds(key, modifiers)


def menu_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.I:
        current_screen = "instructions"
    elif key == arcade.key.P:
        current_screen = "play"
    elif key == arcade.key.ESCAPE:
        exit()


def instructions_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"


def play_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Rock, scissors, paper")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Rock, Paper, Scissors", WIDTH/2, HEIGHT/2+100,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-40,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=20, anchor_x="center")

def draw_play():
    arcade.set_background_color(arcade.color.WHITE)
    
   
def draw_instructions():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2+100,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("Click a button to choose your selection", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


   
    

if __name__ == '__main__':
    setup()
