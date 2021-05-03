# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()



# We may also import the function draw_game directly into the main script's namespace, by using the from command.
from draw import draw_game

def main():
    res = play_game()
    draw_game(res)


# Importing all objects from a module
# We may also use the import * command to import all objects from a specific module, like this:

from draw import *
def main():
    res = play_game()
    draw_game(res)