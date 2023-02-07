import cProfile

cache = {}
def func(n):

    if n == 0 or n == 1:
        return n
        
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n-1) + func(n-2)
            return cache[n]


