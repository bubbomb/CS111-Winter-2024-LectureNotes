from random import randrange, seed, random
from math import sqrt

def calc_pi(n):
    count = 0

    for i in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1.0:
            count += 1
    print(f"With n={n:9}, pi = {4 * count / n}")

if __name__ == "__main__":
    for s in [1,1,2,3]:
        seed(s)
        print(f"seed = {s}:", end=" ")
        for i in range(10):
            print(randrange(1, 100), end=" ")
        print()
    print()
    for i in range(1, 9):
        calc_pi(10 ** i)