import time

def pilingup_v1(input_lines):
    n = int(input_lines[0])

    for i in range(1, n * 2, 2):
        length_stack = int(input_lines[i])
        stack = list(map(int, input_lines[i + 1].split()))
        new_stack = []

        for j in range(length_stack):

            # Check left-most value vs. right-most value. Take smaller of the two
            if stack and stack[0] < stack[-1]:
                new_stack.append(stack[-1])
                stack.pop(-1)
            elif stack and stack[0] > stack[-1]:
                new_stack.append(stack[0])
                stack.pop(0)
            elif stack[0] == stack[-1]:
                new_stack.extend([stack[0], stack[-1]])
                stack.pop(0)
                if stack:
                    stack.pop(-1)

            if j > 0 and new_stack[-1] > new_stack[-2]:
                print("No")
                break
            elif stack == []:
                print("Yes")
                break

def pilingup_v2(input_lines):
    n = int(input_lines[0])

    for i in range(1, n * 2, 2):
        length_stack = int(input_lines[i])
        stack = list(map(int, input_lines[i + 1].split()))
        new_stack = []

        for j in range(length_stack):
            # Check left-most value vs. right-most value. Take smaller of the two
            if stack and stack[0] == stack[-1]:
                new_stack.extend([stack[0], stack[-1]])
                stack.pop(0)
                if stack:
                    stack.pop(-1)
                continue
            if stack and stack[0] < stack[-1]:
                new_stack.append(stack[-1])
                stack.pop(-1)
                continue
            elif stack and stack[0] > stack[-1]:
                new_stack.append(stack[0])
                stack.pop(0)

        sorted_stack = sorted(new_stack, reverse=True)
        if sorted_stack == new_stack:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    input_lines = [
        "2",
        "6",
        "4 3 2 1 3 4",
        "3",
        "1 3 2"
    ]

    start_time = time.time()
    pilingup_v1(input_lines)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    start_time = time.time()
    pilingup_v2(input_lines)
    v2_time = time.time() - start_time
    print(f"v2 Processing time: {v2_time:0.8f}")

