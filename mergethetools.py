import time
def merge_the_tools_v1(string, k):
    #Number of Subsequences
    n = len(string)/k

    #Iterate through string to create substrings
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        print_string=''
        #Iterate through substring to add unique chars to substring_list
        for char in substring:
            if char not in print_string:
                print_string += char
        #Print unique chars for substring
        print(print_string)


if __name__ == '__main__':
    string, k = 'ABBCCCDDEFGH', 3

    start_time = time.time()
    merge_the_tools_v1(string, k)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")
