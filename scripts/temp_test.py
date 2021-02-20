#!/usr/bin/env python
import sys
import cProfile


# nums_squared_lc = [i * 2 for i in range(10000)]
# print(sys.getsizeof(nums_squared_lc))
#
# nums_squared_gc = (i * 2 for i in range(10000))
# print(sys.getsizeof(nums_squared_gc))
#
# cProfile.run('sum([i * 2 for i in range(10000)])')
# cProfile.run('sum((i * 2 for i in range(10000)))')

def h():
    print('To be or not to be')
    yield 5
    yield 6
    print('ok')

n = h()
for i in n:
    print(i)
