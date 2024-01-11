import time

def moddivmod_v1(a, b):
   int_div = a//b
   mod = a%b
   print(f"Integer Division: {int_div}")
   print(f"Modulus: {mod}")
   print(f"Integer Division, Modulus: ({int_div}, {mod})")

if __name__ == '__main__':
    a = 177
    b = 10

    start_time = time.time()
    moddivmod_v1(a,b)
    v1_time = time.time() - start_time
    print(f"v1 Processing time: {v1_time:0.8f}")