import random
from datetime import datetime, timedelta
import time

my_cat = [
    [
        "                      /^--^\    ",
        "                      \____/    ",
        "                     /      \   ",
        "                    |        |  ",
        "                     \__  __/   ",
        "                       / /      ",
        "                      / /       ",
        "                      \ \       ",
        "                       \ \      ",
        "                        \/      "
    ],
    [
        "                      /^--^\       ",
        "                      \____/       ",
        "                     /      \      ",
        "                    |        |     ",
        "                     \__  __/      ",
        "                        \ \        ",
        "                         \ \       ",
        "                         / /       ",
        "                        / /        ",
        "                        \/         "
    ]
]

colorlist = ['31', '32', '33', '34', '35', '36', '37', '91', '92', '93', '94', '95', '96', '97']  # ANSI color codes for text color excluding black
reset_color_output = '\033[0m'
clear_screen = '\n' * 100  # Simulate screen clear with newline characters

def print_cat(cat_index, color_index):
    color_output = '\033[' + colorlist[color_index] + 'm'  # Set text color
    print(clear_screen)  # Clear the screen
    for line in my_cat[cat_index]:
        print(color_output + line)
    print(reset_color_output)  # Reset the color

fps = 5  # Set the desired FPS
frame_time = 1 / fps  # Calculate the time per frame

cat_index = 0  # Initialize the cat index
prev_color_index = None  # Initialize the previous color index

while True:
    # Choose a random color index that is different from the previous one
    color_index = random.choice([idx for idx in range(len(colorlist)) if idx != prev_color_index])
    prev_color_index = color_index
    
    a = random.randint(0, len(colorlist) - 1)
    print_cat(cat_index, color_index)
    cat_index = 1 - cat_index  # Toggle between 0 and 1

    # Wait for one second before printing the next frame
    time.sleep(frame_time)