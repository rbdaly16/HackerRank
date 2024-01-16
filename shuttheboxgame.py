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
    def __init__(self, tiles: list, roll_sum: int):

        """
        Initialize the strategy object
        :param tiles: List of tiles still standing
        :param roll_sum: Sum of dice roll to knock down the tiles
        """

        self.tiles = tiles
        self.roll_sum = roll_sum

    def startlow(self):

        """
        Define the startlow strategy in the Strategy class
        :param tiles: List of tiles still standing
        :param roll_sum: Sum of dice roll to knock down the tiles

        Description:
        Returns a list of tiles.
        Attempts to knock down tiles according to pair addition and single digit match.
        1. Starts with the lowest tile and iterates through the higher tiles in ascending order to
        determine if any larger tile sums with it to the roll_sum. If a pair is found, they are knocked down and that
        new list of tiles is returned.
        2. If not, it steps up to the next higher tile and repeats the process.
        3. If no pair is found, it knocks down the roll_sum number if present and returns the updated list of tiles.
        4. If none of the above, it returns the same list of tiles that was inputted.
        """

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
            # print(f"Roll: {self.roll_sum}, Knocked down: {self.roll_sum}, Strategy: startlow")
            return self.tiles
        else:
            return self.tiles



def shutthebox_v1(start_tiles):
    """
    Define the ShuttheBox game
    :param start_tiles: List of integers, each representing a tile with that number on it

    Rules:
    1. Game has 9 tiles numbered 1-9
    2. Player rolls two dice and sums numbers to total
    3. Player knocks down any amount of tiles that sum to that total. If no tiles can be knocked, sum score
    4. Check if all tiles have been knocked down, if so, we WIN! If not, 2 and 3 again
    """

    num_rolls = 0
    game_over = False
    tiles = start_tiles.copy()

    while game_over == False:
        roll_sum = random.randint(1,6) + random.randint(1,6)
        old_tiles = tiles.copy()

        #Create strategy object
        strategy = Strategy(tiles = tiles, roll_sum = roll_sum)

        #Select strategy
        tiles = strategy.startlow()

        # Game over check -> cond one: all tiles knocked down, cond two: no more tiles could be knocked down
        if not tiles:
            score = 0
            game_outcome = roll_sum, score, num_rolls
            return game_outcome
        elif old_tiles == tiles:
            score = int(''.join(map(str,tiles)))
            game_outcome = roll_sum, score, num_rolls
            return game_outcome

        #Update number of rolls only if it had an effect on the tiles
        num_rolls += 1



if __name__ == '__main__':
    start_tiles = [1,2,3,4,5,6,7,8,9]

    #Run game once
    start_time = time.time()
    roll_sum, score, num_rolls = shutthebox_v1(start_tiles)
    print(roll_sum, score, num_rolls)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    #Check % of wins with 1000 games
    start_time_1000 = time.time()
    num_wins = 0
    scores = []
    for i in range(1000):
        roll_sum, score, num_rolls = shutthebox_v1(start_tiles)
        if score == 0:
            num_wins += 1
        scores.append(score)

    #Obtain stats of 1000 games
    avg_score = sum(scores) / len(scores)
    win_perc = num_wins/len(scores)
    print(f"Winning %: {win_perc}, Avg. Score: {avg_score}")
    v1_time_1000 = time.time() - start_time_1000
    print(f"v1_time_1000 Processing time: {v1_time_1000:0.8f}")


