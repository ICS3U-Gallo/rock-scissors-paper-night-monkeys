import arcade
import random
import math
from random import randint

WIDTH = 1365
HEIGHT = 710

# Variables
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
    elif key == arcade.key.ENTER:
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
    if key == arcade.key.R:
        player = "Pock"
    if key == arcade.key.P:
        player = "Paper"
    if key == arcade.key.S:
        player = "Scissors"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Rock, scissors, paper")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    

    arcade.run()


def draw_menu():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("-- Rock -- Paper -- Scissors --", HEIGHT - 180, WIDTH / 4, arcade.color.WHITE, font_name="garamond", font_size=16)
    arcade.draw_text("Press Enter To Start", HEIGHT - 105, WIDTH / 4.4, arcade.color.WHITE, font_name="garamond", font_size=10)
    arcade.draw_text("Justin, Ethan, Mateo, Shaan", HEIGHT / 60, WIDTH / 2, arcade.color.WHITE, font_name="garamond", font_size=10)
    arcade.draw_text("Press I for info", HEIGHT - 90, WIDTH / 4.8, arcade.color.WHITE, font_name="garamond", font_size=10)


def draw_play():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Choose your move", HEIGHT - 180, WIDTH / 4, arcade.color.WHITE, font_name="garamond", font_size=16)




def draw_instructions():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("Instructions", HEIGHT / 60, WIDTH / 2, arcade.color.WHITE, font_name="garamond", font_size=10)
    arcade.draw_xywh_rectangle_outline(510, 260, 100, 100, arcade.color.WHITE)
    arcade.draw_text("R", HEIGHT - 155, WIDTH / 4.5, arcade.color.WHITE, font_name = "garamond", font_size = 10)
    arcade.draw_xywh_rectangle_outline(630, 260, 100, 100, arcade.color.WHITE)
    arcade.draw_text("P", HEIGHT - 34, WIDTH / 4.5, arcade.color.WHITE, font_name = "garamond", font_size = 10)
    arcade.draw_xywh_rectangle_outline(750, 260, 100, 100, arcade.color.WHITE)
    arcade.draw_text("S", HEIGHT + 85, WIDTH / 4.5, arcade.color.WHITE, font_name = "garamond", font_size = 10)
    arcade.draw_text("Select from the keys:", HEIGHT - 105, WIDTH / 3.6, arcade.color.WHITE, font_name= "garamond", font_size= 14)
    arcade.draw_text("Press ESC to go back", HEIGHT + 525, WIDTH / 2, arcade.color.WHITE, font_name= "garamond", font_size= 10)


# if __name__ == '__main__':
#     setup()
    
    
#     t = ["Rock", "Paper", "Scissors"]
#     computer = t[randint(0, 2)]
#     player = False
#     while player == False:
#         if player == computer:
#             arcade.draw_text("TIE", HEIGHT - 180, WIDTH / 4, arcade.color.WHITE, font_name="garamond", font_size=16)
#         elif player == "Rock":
#             if computer == "Paper":
#                 print("You lose!", computer, "covers", player)
#             else:
#                 print("You win!", player, "smashes", computer)
#         elif player == "Paper":
#             if computer == "Scissors":
#                 print("You lose!", computer, "cut", player)
#             else:
#                 print("You win!", player, "covers", computer)
#         elif player == "Scissors":
#             if computer == "Rock":
#                 print("You lose...", computer, "smashes", player)
#             else:
#                 print("You win!", player, "cut", computer)
#         else:
#             print("That's not a valid play. Check your spelling!")

#         player = False
#         computer = t[randint(0, 2)]

