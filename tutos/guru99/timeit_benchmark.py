import random
import timeit

print("The time taken is ", timeit.timeit(stmt="a=10;b=10;sum=a+b",number=100000000)) # stmt executed 1 000 000 times, optional number
print('-'*72)

def test():
    return random.randint(10, 100)


start_time = timeit.default_timer()
# print("The start time is :", start_time)
test()
print("The time difference is :", timeit.default_timer() - start_time)
print('-'*72)

import_module = "import random"
test_code = """ 
def test():
    print('.')
    return random.randint(10, 100)
"""
print(timeit.repeat(stmt=test_code, setup=import_module, number=1000000, repeat=10))
