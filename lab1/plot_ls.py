import matplotlib.pyplot as plt
from benchmark_ls import *


def plot_results(results, plot_title):
    sizes = [size for size, time in results]
    times = [time for size, time in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, color='b', label='Linear Search') 
    plt.xlabel('Array Size', fontsize=12)
    plt.ylabel('Time Taken (nanoseconds)', fontsize=12)
    plt.title(plot_title, fontsize=14)
    plt.legend()
    plt.savefig(f"{plot_title}.png")

if __name__ == "__main__":
    results = benchmark_search()
    print(results)
    plot_results(results, "Linear Search: Element found in the last index")