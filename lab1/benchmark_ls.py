from linearsearch import search
import random
import time

def benchmark_search():
    sizes = list()
    for i in range (1,10**5,100):
        sizes.append(i) 
    results = []

    for size in sizes:
        arr = list(range(size))
        #target = random.choice(arr)
        #target = (len(arr)//2)
        target = arr[-1]
        
        start_time = time.perf_counter_ns()
        search(arr, size, target)
        elapsed_time = time.perf_counter_ns() - start_time

        results.append((size, elapsed_time))
        print(f"Array Size: {size}, Time Taken: {elapsed_time:.8f} seconds")
    
    return results
if __name__ == "__main__":
    benchmark_search()