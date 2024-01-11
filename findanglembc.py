import time
import math

def find_angle_mbc_v1(AB, BC):
    a = AB
    b = BC

    angle = round(math.degrees(math.atan((a / 2) / (b / 2))))

    print(f"{angle}\u00b0")

if __name__ == '__main__':
    AB = 10
    BC = 7

    start_time = time.time()
    find_angle_mbc_v1(AB, BC)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")