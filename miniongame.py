def minion_game(string):
    # Defines vowels
    vowels = 'AEIOU'
    stuart_tracking = []
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    # Iterates over string, finds length of substrings, then sums these together
    kevin_score = sum([length - char for char, char_value in enumerate(string) if char_value in vowels])
    stuart_score = sum([length - char for char, char_value in enumerate(string) if char_value not in vowels])

    # Assign and print winner
    winner = 'Stuart' if stuart_score > kevin_score else 'Kevin' if kevin_score > stuart_score else 'Draw'
    if winner == 'Draw':
        print(winner)
    else:
        print(winner + " " + str(max(stuart_score, kevin_score)))


if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)