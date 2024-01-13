"""
Shut the Box Game
Rules:
1. Game has 9 tiles numbered 1-9
2. Player rolls two dice and sums numbers to total
3. Player knocks down any amount of tiles that sum to that total. If no tiles can be knocked, sum score
4. Check if all tiles have been knocked down, if so, we WIN! If not, 2 and 3 again
"""

import time
import itertools
import random


class Strategy(object):
    def __init__(self, tiles, roll_sum):
        self.tiles = tiles
        self.roll_sum = roll_sum

    def __startlow__(self):
        j = 0

        for low_tile in self.tiles:
            j += 1
            for tile in self.tiles[j:]:
                if low_tile + tile == self.roll_sum:
                    self.tiles.remove(low_tile)
                    self.tiles.remove(tile)
                    print(f"You rolled a {self.roll_sum} so I knocked down {low_tile} and {tile} using startlow strategy.")
                    return self.tiles



def shutthebox_v1(tiles):
    num_rolls = 0
    game_over = False

    while game_over == False:
        roll_sum = random.randint(1,6) + random.randint(1,6)
        num_rolls += 1

        #Create strategy object
        strat = Strategy(tiles = tiles, roll_sum = roll_sum)

        #Select strategy
        old_tiles = tiles.copy()
        strat.__startlow__()

        #Check to see if no tiles were able to be knocked down
        if old_tiles == tiles:
            return print(f"No more tiles can be knocked down. Here is your final score: {''.join(map(str,tiles))}.")

        #Check to see if all tiles have been knocked down
        if not tiles:
            return f"The game is over! Your victory took {num_rolls} rolls! Congratulations!"





if __name__ == '__main__':
    tiles = [1,2,3,4,5,6,7,8,9]
    start_time = time.time()
    shutthebox_v1(tiles)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")
