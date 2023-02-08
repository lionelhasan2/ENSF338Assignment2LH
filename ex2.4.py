
import sys
import json
import timeit
import matplotlib.pyplot as plt
import random
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pivot_index = random.randint(low,high) #used to generate a random integer between and including the start and end of our array
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index] #swaps the index of the randomly selected pivot and the start of our array 
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi+1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

#Part 4
with open("ex2.json", "r") as file:
    data = json.load(file)

timings = []
for instance in data:
    time2 = timeit.timeit(lambda: func1(instance, 0, len(instance)-1), number=1)
    timings.append(time2)
    print("Time taken for each instance:", time2, "seconds")

plt.plot(timings)
plt.xlabel("Instance Number")
plt.ylabel("Time Taken (Seconds)")
plt.title("Time Taken to Sort Each Instance Within the Json File")
plt.show()

