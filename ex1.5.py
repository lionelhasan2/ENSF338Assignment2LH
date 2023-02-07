import timeit
import matplotlib.pyplot as plt
cache = {}

def func(n):
    if n == 0 or n == 1:
        return n
        
    else:
        return func(n-1) + func(n-2)

def genfunc() :
    rez =[]
    for i in range(35):
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

def genfunc2() :
    rez =[]
    for i in range(35):
        rez.append(func2(i)) 

timetaken =timeit.timeit(lambda: genfunc2(), number =1 )
print(timetaken)
timetaken2 = timeit.timeit(lambda: genfunc(), number =1 )
print(timetaken2)


fig, ax = plt.subplots()
timetake = [timetaken,timetaken2]
print(timetake)
labels = ["Optimized", "Unoptimized"]
plt.bar(labels,timetake)
plt.ylim(0, 6)
ax.set_ylabel("Time taken (s)")

plt.show()


