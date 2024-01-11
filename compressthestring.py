import time
from itertools import groupby

def compressthestring_v1(input_string):
    print_string = ''
    i = 0

    while i < len(input_string):
        char = input_string[i]
        #Not doing for char in input_string so that I can check the next char in the string
        j = i+1
        char_count = 1

       #Check how many consecutive chars are same and update char_count
        while j < len(input_string) and input_string[j] == char:
            char_count += 1
            j += 1

        #Add char_count and char to the string
        print_string += "("+str(char_count)+", "+char+") "
        i = j
    print(print_string)

def compressthestring_v2(input_string):
    from itertools import groupby

    s = input_string
    final_list = [(len(list(group)), int(key)) for key, group in groupby(s)]

    print(*final_list)


if __name__ == '__main__':
    input_string = '1222311'

    start_time = time.time()
    compressthestring_v1(input_string)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    start_time = time.time()
    compressthestring_v2(input_string)
    v2_time = time.time() - start_time
    print(f"v2 Processing time: {v2_time:0.8f}")