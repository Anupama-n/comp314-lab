from quick_sort import quick_sort
import random
import time
import sys


sys.setrecursionlimit(5000)
def benchmark_quick_sort():
    sizes = list()
    for i in range(1,3001,10):  
        sizes.append(i)
    results = []

    for size in sizes:
        #arr = random.sample(range(size), size)
        sorted_case = list(range(size))
        #reverse_case = list(range(size, 0, -1))
        #random_case_with_repetition = random.sample(range(size), size)
        
        start_time = time.perf_counter_ns()
        #quick_sort(random_case_with_repetition, 0, len(random_case_with_repetition) - 1)
        #quick_sort(reverse_case, 0, len(reverse_case) - 1)
        #quick_sort(arr, 0, len(arr) - 1)
        quick_sort(sorted_case, 0, len(sorted_case) - 1)
        
        elapsed_time = time.perf_counter_ns() - start_time

        results.append((size, elapsed_time))
        print(f"Array Size: {size}, Time Taken: {elapsed_time:.8f} nanoseconds")
    
    return results

if __name__ == "__main__":
    benchmark_quick_sort()
