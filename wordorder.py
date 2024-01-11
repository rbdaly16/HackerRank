import time

def wordorder_v1(input_strings):
    n_strings = len(input_strings)

    strings = {}

    for i in range(n_strings):
        word = input_strings[i]
        if word in strings:
            strings[word] += 1
        else:
            strings[word] = 1
    print(len(strings))
    print(' '.join(map(str,strings.values())))

if __name__ == '__main__':
    # Create a list of strings
    input_strings = [
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ]

    start_time = time.time()
    # Use the list of strings as input to the function
    wordorder_v1(input_strings)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")
