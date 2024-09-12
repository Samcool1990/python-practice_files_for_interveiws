# Fastapi Pydantic
# loggers using yml
# multiporcessing
# multithreading
# patching on runtime: while testing your request an url & you get the response after getting the
# response you do patching on run time


# multiporcessing
import multiprocessing
import time


def worker_sum_of_squares(start, end):
    """Worker function to compute the sum of squares for a given range."""
    result = sum(i * i for i in range(start, end))
    return result


def custom_multiprocessor(num_processes=4, range_end=10_000_000):
    """Custom multiprocessing function to parallelize sum of squares computation."""
    range_per_process = range_end // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Create tasks by splitting the range into sub-ranges for each process
    tasks = [
        (i * range_per_process, (i + 1) * range_per_process)
        for i in range(num_processes)
    ]

    # Start timing
    start_time = time.time()

    # Distribute the work among the processes and collect results
    results = pool.starmap(worker_sum_of_squares, tasks)

    # Combine the results from all processes
    total_sum = sum(results)

    # End timing
    end_time = time.time()

    pool.close()
    pool.join()

    print(f"Total sum of squares: {total_sum}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.4f} seconds")


# Example usage
if __name__ == "__main__":
    custom_multiprocessor(num_processes=4, range_end=10_000_000)


# multithreading
import threading
import time
import requests


def download_url(url):
    """Worker function to download the content of a URL."""
    response = requests.get(url)
    print(f"Downloaded {len(response.content)} bytes from {url}")


def custom_multithreader(urls, num_threads=4):
    """Custom multithreading function to download data from multiple URLs concurrently."""
    threads = []
    start_time = time.time()

    # Create and start threads
    for i in range(num_threads):
        # Divide the URLs between threads
        thread_urls = urls[i::num_threads]
        thread = threading.Thread(target=download_worker, args=(thread_urls,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken with multithreading: {end_time - start_time:.4f} seconds")


def download_worker(urls):
    """Worker function to handle the downloading task in a thread."""
    for url in urls:
        download_url(url)


# Example usage
if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.djangoproject.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
    ]
    custom_multithreader(urls, num_threads=3)
