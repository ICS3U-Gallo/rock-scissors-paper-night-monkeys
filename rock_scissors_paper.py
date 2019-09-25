import arcade

# screen dimension

WIDTH = 1365
HEIGHT = 710

# variables

current_screen = "play"
x = 0
y = 0
xx = 0

# open window

arcade.open_window(WIDTH, HEIGHT, "Rock Paper Scissors")
arcade.set_background_color(arcade.color.WOOD_BROWN)

# render    

arcade.start_render()

# draw

arcade.draw_text("Rock Paper Scissors", HEIGHT - 700, WIDTH / 2, arcade.color.BLACK, font_size=20,font_name="garamond")





arcade.finish()

arcade.run()


t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]


player = False

while player == False:
    player = input("Rock, Paper, Scissors?: ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
   
    player = False
    computer = t[randint(0,2)]


