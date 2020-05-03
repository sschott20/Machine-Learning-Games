import numpy as np
import player
import random
import time
import sys, os
from array_backed_grid import display
MAP_SIZE = 15


def start_game(maze_template, delay=0, output=False):
    game_end = False
    display_grids = []

    player_position = [random.randint(1, MAP_SIZE - 2), random.randint(1, MAP_SIZE - 2)]
    goal_position = [random.randint(1, MAP_SIZE - 2), random.randint(1, MAP_SIZE - 2)]

    # player_position = [1, 1]
    # goal_position = [7, 7]
    if goal_position == player_position:
        goal_position[0] += 1


    maze_display = np.copy(maze_template)

    maze_display[goal_position[0], goal_position[1]] = 2
    maze_display[player_position[0], player_position[1]] = 1

    player.new_game()
    if output:
        # print(maze_display)
        # time.sleep(delay)
        # print("\n" * 10)
        display_grids.append(maze_display)
    while not game_end:


        action = player.update(maze_template, player_position, goal_position)


        if action == "left":
            player_position[1] -= 1
        elif action == "right":
            player_position[1] += 1
        elif action == "up":
            player_position[0] -= 1
        elif action == "down":
            player_position[0] += 1
        elif action == "end":
            game_end = True
            if output:
                display(display_grids)
            break

        # Prep maze to be displayed to the observer
        maze_display = np.copy(maze_template)
        maze_display[goal_position[0], goal_position[1]] = 2
        maze_display[player_position[0], player_position[1]] = 1
        if output:
            # print(maze_display)
            display_grids.append(maze_display)
            time.sleep(delay)
            # print("\n" * 10)


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    actions = ["left", "right", "up", "down"]
    player = player.Player(actions)
    maze_template = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)
    maze_template[0, :] = 3
    maze_template[1:, 0] = 3
    maze_template[1:, -1] = 3
    maze_template[-1, 1:-1] = 3

    print("Training Start")

    blockPrint()
    for i in range(10000):
        if i % 5000 == 0:
            enablePrint()
            print(i)
            start_game(delay=0, output=True, maze_template=maze_template)
            blockPrint()
        else:
            start_game(delay=0, output=False, maze_template=maze_template)
    enablePrint()

    print("Training Complete")

    for i in range(1):
        start_game(delay=0, output=True, maze_template=maze_template)

    player.output_table()
