import random
import time
import tracemalloc

def selection(array):
    length = len(array)
    for i in range(0, length):
        min_number = i
        for j in range(i+1, length):
            if array[j] < array[min_number]:
                min_number = j
        (array[i], array[min_number]) = (array[min_number], array[i])


arr = []
n = int(input("Write the length of array:"))
for i in range(n):
    arr.append(random.randint(0, 1000))
# print("Array before Selection Sort")
# print(arr)

start_time = time.time()
selection(arr)
finish_time = time.time()
memory = tracemalloc.get_tracemalloc_memory()

print("\nTime Bubble Sort: %s" % (finish_time - start_time))
print("Memory Bubble Sort: %d" % memory)
# print("Array after Selection Sort")
# print(arr)

