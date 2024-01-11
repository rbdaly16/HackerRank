import time
import itertools

def has_a_in_tuple(tup):
   return 'a' in tup

def iterablesanditerators_v1(input_lines):
    num_letters = input_lines[0]
    letters = input_lines[1].replace(" ","")
    num_indices = int(input_lines[2])

    #Create all possible combinations
    test_groups = list(itertools.combinations(letters, num_indices))

    #Create list of only combinations that include 'a'
    filtered_list = list(itertools.filterfalse(lambda x: not has_a_in_tuple(x), test_groups))

    #How many combinations are presetn and how many contain 'a'
    num_combs = len(test_groups)
    num_a_combs = len(filtered_list)

    #Calculate probability
    prob_a = num_a_combs / num_combs

    return print(round(prob_a, 4))


if __name__ == '__main__':
    input_lines = ['4',
                   'a a c d',
                   '2']
    start_time = time.time()
    iterablesanditerators_v1(input_lines)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")