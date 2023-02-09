import timeit
import matplotlib.pyplot as plt
cache = {}

def func(n):
    if n == 0 or n == 1:
        return n
        
    else:
        return func(n-1) + func(n-2)

def genfunc(n) :
    rez =[]
    for i in range(n):
        rez.append(func(i)) 
    

def func2(n):

    if n == 0 or n == 1:
        return n
        
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = func2(n-1) + func2(n-2)
            return cache[n]

def genfunc2(n) :
    rez =[]
    for i in range(n):
        rez.append(func2(i)) 

ttlist1 =[]
for i in range(35):
    k = timeit.timeit(lambda: genfunc2(i), number =1 )
    ttlist1.append(k)


ttlist2 =[]
for i in range(35):
    k = timeit.timeit(lambda: genfunc(i), number =1 )
    ttlist2.append(k)


num_list = []
for i in range(35):
    num_list.append(i)


plt.plot(num_list,ttlist1, label = "Optimized")
plt.plot(num_list,ttlist2, label = "Unoptimized")
plt.ylabel("Seconds")
plt.xlabel("Instances")
plt.legend()
plt.show()

