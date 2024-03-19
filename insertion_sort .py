import random
import time
import tracemalloc

def insertion(array):
    length = len(array)
    for i in range(0, length):
        key = array[i]
        pos = i
        while (pos > 0) and (array[pos-1] > key):
            (array[pos-1], array[pos]) = (array[pos], array[pos-1])
            pos = pos - 1
        array[pos] = key

arr = []
n = int(input("Write the length of array:"))
for i in range(n):
    arr.append(random.randint(0, 1000))
# print("Array before Insertion Sort")
# print(arr)

start_time = time.time()
insertion(arr)
finish_time = time.time()
memory = tracemalloc.get_tracemalloc_memory()

print("\nTime Bubble Sort: %s" % (finish_time - start_time))
print("Memory Bubble Sort: %d" % memory)
# print("Array after Insertion Sort")
# print(arr)

