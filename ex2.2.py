import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
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

#Part 2
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

