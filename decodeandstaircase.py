import time


def is_staircase(nums):
    col_length = 0
    staircase = []
    relevant_keys = []
    input_list = nums.copy()

    while len(input_list) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(input_list.pop(0))

            if (len(input_list) == 0):
                if i < col_length - 1:
                    return False
                staircase.append(column)
                relevant_keys.append(column[-1])
                return relevant_keys
        staircase.append(column)
        relevant_keys.append(column[-1])

if __name__ == '__main__':
    # Specify the file path
    file_path = '/Users/robertdaly/Desktop/coding_qual_input.txt'

    # Initialize an empty dictionary to store the data
    message_dict = {}

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into the count and the message
            count, message = line.strip().split(' ', 1)

            # Convert count to an integer
            count = int(count)

            # Add the key-value pair to the dictionary
            message_dict[count] = message

            # Obtain list of dict keys
            dict_keys = sorted(list(message_dict.keys()))



        input_nums = dict_keys
        relevant_keys = is_staircase(input_nums)
        # Create string to return
        print_string = ""
        for num in relevant_keys:
            print_string += " " + message_dict[num]

        print(print_string)







# def decode(message_file):
#
#     # Define function to create a staircase
#     def is_staircase(nums):
#         # Initialize variables
#         col_length = 0
#         staircase = []
#         relevant_keys = []
#         input_list = nums.copy()
#
#         # Loop until input_list is empty
#         while len(input_list) > 0:
#             col_length = col_length + 1
#             column = []
#
#             # Build a column for the current level
#             for i in range(0, col_length):
#                 column.append(input_list.pop(0))
#
#                 # Check if all numbers have been used
#                 if (len(input_list) == 0):
#                     # If all numbers used, confirm that it is a proper staircase
#                     if i < col_length - 1:
#                         return False
#                     # If it is a proper staircase, add column to staircase, add last integer to relevant_keys, and return relevant_keys
#                     staircase.append(column)
#                     relevant_keys.append(column[-1])
#                     return relevant_keys
#             # If not all numbers checked yet, append column to staircase and last integer of column to relevant_keys
#             staircase.append(column)
#             relevant_keys.append(column[-1])
#
#     # Initialize an empty dictionary to store the data
#     message_dict = {}
#
#     # Open the file in read mode
#     with open(file_path, 'r') as file:
#         # Read each line from the file
#         for line in file:
#             # Split the line into the count and the message
#             count, message = line.strip().split(' ', 1)
#
#             # Convert count to an integer
#             count = int(count)
#
#             # Add the key-value pair to the dictionary
#             message_dict[count] = message
#
#             # Obtain list of dict keys
#             dict_keys = sorted(list(message_dict.keys()))
#
#         input_nums = dict_keys
#         relevant_keys = is_staircase(input_nums)
#         # Create string to return
#         print_string = ""
#         for num in relevant_keys:
#             print_string += " " + message_dict[num]
#
#         # Print string
#         print(print_string)
