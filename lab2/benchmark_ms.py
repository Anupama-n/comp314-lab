import random
import time
import sys
import math
from merge_sort import *

sys.setrecursionlimit(5000)

def benchmark_merge_sort():
    sizes = list()
    for i in range(1, 3001, 10): 
        sizes.append(i)
    
    results = []

    for size in sizes:
        #sorted_case = list(range(size))  
        #reverse_case = list(range(size, 0, -1))  
        #random_case_with_repetition = random.sample(range(size), size)  
        arr = random.sample(range(size), size)
        
        start_time = time.perf_counter_ns()
        #merge_sort(sorted_case, 0, len(sorted_case) - 1)
        #merge_sort(reverse_case, 0, len(reverse_case) - 1)
        #merge_sort(random_case_with_repetition, 0, len(random_case_with_repetition) - 1)
        merge_sort(arr, 0, len(arr) - 1)
        
        elapsed_time = time.perf_counter_ns() - start_time

        results.append((size, elapsed_time))
        print(f"Array Size: {size}, Time Taken: {elapsed_time:.8f} nanoseconds")
    
    return results

if __name__ == "__main__":
    benchmark_merge_sort()
