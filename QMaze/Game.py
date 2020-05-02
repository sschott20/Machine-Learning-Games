import numpy as np
from player import Player
import random
import time


def start_game():
    MAP_SIZE = 9
    actions = ["left", "right", "up", "down"]

    player_position = [random.randint(1, MAP_SIZE - 2), random.randint(0, MAP_SIZE - 2)]
    goal_position = [random.randint(0, MAP_SIZE - 2), random.randint(0, MAP_SIZE - 2)]

    game_end = False

    maze_template = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)
    maze_template[0, :] = -1000
    maze_template[1:, 0] = -1000
    maze_template[1:, -1] = -1000
    maze_template[-1, 1:-1] = -1000
    maze_display = np.copy(maze_template)

    maze_display[goal_position[0], goal_position[1]] = 1000
    maze_display[player_position[0], player_position[1]] = 1

    player = Player(actions)

    while not game_end:
        print("\n" * 10)
        # action = player.update()
        action = random.choice(actions)

        if action == "left":
            player_position[1] -= 1
        elif action == "right":
            player_position[1] += 1
        elif action == "up":
            player_position[0] += 1
        elif action == "down":
            player_position[0] -= 1

        # Prep maze to be displayed to the observer
        maze_display = np.copy(maze_template)
        maze_display[goal_position[0], goal_position[1]] = 100
        maze_display[player_position[0], player_position[1]] = 1

        print(player_position)
        print(maze_display)
        time.sleep(4)
if __name__ == '__main__':
    start_game()
