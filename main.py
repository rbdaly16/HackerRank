
#array, A, B
import time
from noidea import happiness_counter

if __name__ == '__main__':
    initial_array = [1, 5, 3]
    happy_list = set([3, 1])
    sad_list = set([5, 7])

    start_time = time.time()
    happiness_counter(f"{len(initial_array)} {len(happy_list)}\n{initial_array}\n{happy_list}\n{sad_list}")
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")