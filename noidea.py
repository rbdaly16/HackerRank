import time

def happiness_counter(the_array, happy_list, sad_list):
    happiness = sum([the_array.count(n) for n in happy_list])
    sadness = sum([the_array.count(n) for n in sad_list])
    final_happiness = happiness - sadness
    print(final_happiness)

def happiness_counter_v2(the_array, happy_list, sad_list):
    happiness = 0
    sadness = 0
    for n in the_array:
        if n in happy_list:
            happiness += 1
        elif n in sad_list:
            sadness += 1
    final_happiness = happiness - sadness
    print(final_happiness)

def happiness_counter_v3(the_array, happy_list, sad_list):
    happiness = 0
    sadness = 0
    happy_done = []
    sad_done = []
    for n in the_array:
        if n in happy_done:
            happiness += 1
        elif n in happy_list:
            happiness += 1
            happy_done.append(n)
        elif n in sad_done:
            sadness += 1
        elif n in sad_list:
            sadness += 1
            sad_done.append(n)
    final_happiness = happiness - sadness
    print(final_happiness)


if __name__ == '__main__':
    initial_array = [1, 5, 3]
    happy_list = [3, 1]
    sad_list = [5, 7]

    start_time = time.time()
    happiness_counter(initial_array, happy_list, sad_list)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    start_time = time.time()
    happiness_counter_v2(initial_array, happy_list, sad_list)
    v2_time = time.time() - start_time
    print(f"v2 Processing time: {v2_time:0.8f}")

    start_time = time.time()
    happiness_counter_v3(initial_array, happy_list, sad_list)
    v3_time = time.time() - start_time
    print(f"v3 Processing time: {v3_time:0.8f}")

