import arcade

# screen dimension

WIDTH = 1365
HEIGHT = 710

# variables

current_screen = "play"
x = 0
y = 0
xx = 0
JzmR03-patch-1
# open window

arcade.open_window(WIDTH, HEIGHT, "Rock Paper Scissors")
arcade.set_background_color(arcade.color.WOOD_BROWN)

# render    

arcade.start_render()

# draw

arcade.draw_text("Rock Paper Scissors", HEIGHT - 700, WIDTH / 2, arcade.color.BLACK, font_size=20,font_name="garamond")





arcade.finish_render()

arcade.run()
