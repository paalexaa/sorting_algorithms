import random
import time
import tracemalloc

def bubble(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])


arr = []
n = int(input("Write the length of array:"))
for i in range(n):
    arr.append(random.randint(0, 1000))
# print("Array before Bubble Sort")
# print(arr)

start_time = time.time()
bubble(arr)
finish_time = time.time()
memory = tracemalloc.get_tracemalloc_memory()

print("\nTime Bubble Sort: %s" % (finish_time - start_time))
print("Memory Bubble Sort: %d" % memory)
# print("Array after Bubble Sort")
# print(arr)