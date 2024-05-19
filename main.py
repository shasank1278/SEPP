import matplotlib.pyplot as plt
import numpy as np
import time


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


input_sizes = [100, 200, 300, 400, 500]  # Different input sizes
time_taken = []

for n in input_sizes:
    arr = list(range(n))  # Generate a sorted list of size n
    x = n // 2  # Element to search (middle element)

    start = time.time()
    result = binary_search(arr, 0, len(arr) - 1, x)
    end = time.time()

    time_taken.append(end - start)

plt.plot(input_sizes, time_taken)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Binary Search')
plt.show()

