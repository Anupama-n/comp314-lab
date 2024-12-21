import time
import random
from binarysearch import search

def benchmark_search():
    sizes = list()
    for i in range (1,10**5,100):
        sizes.append(i)
    results = []

    for size in sizes:
        arr = list(range(size))
        target = random.choice(arr) 
        #target = (len(arr)//2)        
        start_time = time.perf_counter_ns()
        search(arr, target)
        elapsed_time = time.perf_counter_ns() - start_time 

        results.append((size, elapsed_time))
        # print(f"Array Size: {size}, Time Taken: {elapsed_time:.8f} nanoseconds")
    
    return results


if __name__ == "__main__":
    benchmark_search()