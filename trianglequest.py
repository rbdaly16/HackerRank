import time

def triangle_v1(N):
    for i in range(1, N):
        print(f"{ascii(i)*i}")

if __name__ == '__main__':
    N = 5

    start_time = time.time()
    triangle_v1(N)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

def triangle2_v1(N):
    for i in range(1, N + 1):
        print_string = ''
        for j in range (1,i+1):
            print_string += str(j)
        for x in range (i-1,0, -1):
            print_string += str(x)
        print(print_string)

def triangle2_v2(N):
    print_string = ''
    for i in range(1, N + 1):
        print_string += str(i)
        print(f"{print_string}{print_string[::-1][1:]}")


if __name__ == '__main__':
    N = 5

    start_time = time.time()
    triangle2_v1(N)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")

    start_time = time.time()
    triangle2_v2(N)
    v2_time = time.time() - start_time
    print(f"v2 Processing time: {v2_time:0.8f}")