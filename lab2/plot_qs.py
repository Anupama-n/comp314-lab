import matplotlib.pyplot as plt
from benchmark_qs import *

def plot_results(results, plot_title):
    sizes = [size for size, time in results]
    times = [time for size, time in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, color='r', label='QuickSort') 
    plt.xlabel('Array Size', fontsize=12)
    plt.ylabel('Time Taken (nanoseconds)', fontsize=12)
    plt.title(plot_title, fontsize=14)
    plt.legend()
    plt.savefig(f"{plot_title}.png")
    plt.show() 

if __name__ == "__main__":
    results = benchmark_quick_sort() 
    print(results)
    plot_results(results, "QuickSort: Sorted Case")
