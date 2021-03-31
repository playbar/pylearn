import math
import time
from numba import njit, prange

@njit
def is_prime(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num) + 1), 2):
        if not num % div:
            return False
    return True

@njit(parallel=True)
def run_program(N):
    total = 0
    for i in prange(N):
        if is_prime(i):
            total += 1
    return total


if __name__ == "__main__":
    print(f"begin")
    N = 10000000
    start = time.time()
    total = run_program(N)
    end = time.time()
    print(f"total prime num is {total}")
    print(f"cost {end - start}s")

