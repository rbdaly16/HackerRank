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
        self.tiles = tiles.copy()
        self.roll_sum = roll_sum

    def __startlow__(self):
        j = 0

        #iterate through list starting with lowest number
        for low_tile in self.tiles:
            j += 1
            for tile in self.tiles[j:]:
                if low_tile + tile == self.roll_sum:
                    self.tiles.remove(low_tile)
                    self.tiles.remove(tile)
                    # print(f"Roll: {self.roll_sum}, Knocked down: {low_tile} and {tile}, Strategy: startlow.")
                    return self.tiles
        if self.roll_sum in self.tiles:
            self.tiles.remove(self.roll_sum)
            return self. tiles



def shutthebox_v1(start_tiles):
    num_rolls = 0
    game_over = False
    tiles = start_tiles

    while game_over == False:
        roll_sum = random.randint(1,6) + random.randint(1,6)
        num_rolls += 1

        #Create strategy object
        strat = Strategy(tiles = tiles, roll_sum = roll_sum)

        #Select strategy
        old_tiles = tiles.copy()
        strat.__startlow__()

        # Check to see if all tiles have been knocked down
        if not tiles:
            score = 0
            return f"The game is over! Your victory took {num_rolls} rolls! Congratulations!", score

        #Check to see if no tiles were able to be knocked down
        if old_tiles == tiles:
            score = ''.join(map(str,tiles))
            return f"No more tiles can be knocked down with a roll of {roll_sum}. Here is your final score:", score







if __name__ == '__main__':
    start_tiles = [1,2,3,4,5,6,7,8,9]

    #Run game once
    start_time = time.time()
    result, score_value = shutthebox_v1(start_tiles)
    print(result, score_value)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    #Check % of wins with 1000 games
    start_time_1000 = time.time()
    num_wins = 0
    scores = []
    for i in range(1000):
        result, score_value = shutthebox_v1(start_tiles)
        if score_value == 0:
            num_wins += 1
        scores.append(score_value)

    #Obtain stats of 1000 games
    avg_score = sum(map(int,scores)) / len(scores)
    win_perc = num_wins/len(scores)
    print(f"Winning %: {num_wins}, Avg. Score: {avg_score}")
    v1_time_1000 = time.time() - start_time_1000
    print(f"v1_time_1000 Processing time: {v1_time_1000:0.8f}")


