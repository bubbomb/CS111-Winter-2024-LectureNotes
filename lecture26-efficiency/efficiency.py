# import timeit


def exp(b, n):
  if n == 0:
    return 1
  else:
    return b * exp(b, n-1)


square = lambda x: x * x
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1) 

def overlap(a, b):
    """
    >>> overlap([3, 5, 7, 6], [4, 5, 6, 5])
    3
    """
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count


def virfib(n):
    if n in {0,1}:
        return n

    total = virfib(n-1) + virfib(n-2)
    return total


def cache_virfib(n, cache={}):
    if not cache:
       cache = {0:0, 1:1}

    if n in cache:
        return cache[n]
    else:
       cache[n] = cache_virfib(n-1, cache) + cache_virfib(n-2, cache)

    return cache[n]

       
   

import timeit
print('------------------------------------------------------')
# print('------------ exp -------------')
# num = 1
# exponent = 150

# print(f'num:{num}, exponent:{exponent}')
# print(timeit.timeit(f'exp({num},{exponent})', globals=globals(), number=10000))
# print(timeit.timeit(f'exp_fast({num},{exponent})', globals=globals(), number=10000))

# print()
# print('------------ overlap -------------')


# list2 = [x for x in range(10)]
# list1 = [x for x in range(10)]

# print(timeit.timeit(f'overlap({list1}, {list2})', globals=globals(), number=1000))

print('------------ virfib -------------')

virfib_num = 30

print(timeit.timeit(f'virfib({virfib_num})', globals=globals(), number=1))
print(timeit.timeit(f'cache_virfib({virfib_num})', globals=globals(), number=1))