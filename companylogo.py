import time
from itertools import groupby

def companylogo_v1(input_string):
    letter_count = {}

    for char in input_string:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

    letter_count_sorted = sorted(letter_count.items(), key=lambda item:(-item[1], item[0]))

    for pair in letter_count_sorted[:3]:
       print(pair[0], pair[1])

def companylogo_v2(input_string):
    s = sorted(input_string)
    char_occurence = [(len(list(group)), key) for key, group in groupby(s)]
    # print(s)
    char_occurence_sorted = sorted(char_occurence, key = lambda item:(-item[0], item[1]))

    for char in char_occurence_sorted[:3]:
        print(char[1],char[0])


if __name__ == '__main__':
    # input_string = 'qwertyuiopasdfghjklzxcvbnm'
    input_string = 'aabbbccde'
    start_time = time.time()
    companylogo_v1(input_string)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    start_time = time.time()
    companylogo_v2(input_string)
    v2_time = time.time() - start_time
    print(f"v2 Processing time: {v2_time:0.8f}")

