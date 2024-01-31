import numpy as np
import time
import matplotlib.pyplot as plt


def heapify(arr, n, i):
    # current as largest, calc. index of left and right child nodes
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # if the left child exists &  greater than the current largest
    if left < n and arr[i] < arr[left]:
        largest = left

    # if the right child exists & greater than the current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If the largest is not the current node, swap the values and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    # heapifying each non-leaf node in reverse order
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # extract one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr  #   sorted array


"""
The input array to be sorted. Returns: sorted array.
    """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] #getting pivot as 1st el.
        # Divide into two: elements less than or equal to the pivot (less)
        # and elements greater than the pivot (greater)
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


"""Getting start time, sort copy of array, get end time.
Calculate exec. time + length of sorted array """        
def measure_time_and_steps(sort_function, array):
    start = time.time()
    sorted_array = sort_function(array.copy())
    end = time.time()
    execution_time = end - start
    return execution_time, len(sorted_array)

input_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
steps_heapsort = []
steps_quicksort = []

for size in input_sizes:
    # sorted array (asc)
    sorted_array = np.arange(size)
    # Shuffle/random arr
    np.random.shuffle(sorted_array)

    # Time and steps for heapsort on a random array
    time_heapsort_random, steps_heapsort_random = measure_time_and_steps(heapsort, sorted_array.copy())
    steps_heapsort.append(steps_heapsort_random)

    # Time and steps for quicksort on a random array
    time_quicksort_random, steps_quicksort_random = measure_time_and_steps(quicksort, sorted_array.copy())
    steps_quicksort.append(steps_quicksort_random)

    # Time and steps for heapsort on a reversed array (worst-case)
    time_heapsort_worst, steps_heapsort_worst = measure_time_and_steps(heapsort, np.arange(size)[::-1])
    steps_heapsort_worst = np.full_like(input_sizes, steps_heapsort_worst)  # Repeat the value for all input sizes
    
    # Time and steps for quicksort on a reversed array (worst-case)
    time_quicksort_worst, steps_quicksort_worst = measure_time_and_steps(quicksort, np.arange(size)[::-1])
    steps_quicksort_worst = np.full_like(input_sizes, steps_quicksort_worst)  # Repeat the value for all input sizes


    # Print results
    print(f"Size {size}:"
          f"\n  Heapsort time (random) = {time_heapsort_random}, Quicksort time (random) = {time_quicksort_random}"
          f"\n  Heapsort steps (random) = {steps_heapsort_random}, Quicksort steps (random) = {steps_quicksort_random}"
          f"\n  Heapsort time (worst) = {time_heapsort_worst}, Quicksort time (worst) = {time_quicksort_worst}"
          f"\n  Heapsort steps (worst) = {steps_heapsort_worst}, Quicksort steps (worst) = {steps_quicksort_worst}\n")




# Plotting combined results with logarithmic scale on y-axis
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, steps_heapsort, label='Heapsort (Random)')
plt.plot(input_sizes, steps_quicksort, label='Quicksort (Random)')


plt.plot(input_sizes, steps_heapsort_worst, label='Heapsort (Worst-case)')
plt.plot(input_sizes, steps_quicksort_worst, label='Quicksort (Worst-case)')

plt.xlabel('Input Size (n)')
plt.ylabel('Number of Steps')
plt.title('Comparison of Heapsort and Quicksort')
plt.legend()
plt.yscale('log')  # Set logarithmic scale on the y-axis
plt.show()



