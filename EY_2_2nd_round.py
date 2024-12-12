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



#Question:  patching on runtime: while testing your request an url & you get the response after getting the 
# response you do patching on run time

# Answer:
# Runtime patching during testing is a common practice, especially when using tools like unittest.mock in 
# Python. The idea is to modify an object or method's behavior at runtime during tests. This is particularly 
# useful when you want to simulate or manipulate data after receiving a response from an API or URL.

# Example:
# Scenario
# You have a function fetch_data that makes an API call and returns a response.
# After receiving the response, you modify or "patch" a specific behavior in runtime to adjust for testing 
# conditions.
    

import requests
from unittest.mock import patch

# Function to be tested
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the response is JSON
    return None

# Test function with runtime patching
def test_fetch_data_with_patching():
    # Mocked response data
    mocked_response = {
        "id": 1,
        "name": "Test User",
        "status": "active"
    }

    # Step 1: Patch 'requests.get' to return a mock response
    with patch('requests.get') as mock_get:
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        # Mock the response from the API
        mock_get.return_value = MockResponse(mocked_response, 200)

        # Step 2: Fetch the data (will use the mocked response)
        url = "https://api.example.com/user"
        response = fetch_data(url)

        # Step 3: Patch runtime behavior (e.g., modifying the response)
        if "status" in response and response["status"] == "active":
            response["status"] = "inactive"

        # Assertions
        assert response["status"] == "inactive"
        assert response["name"] == "Test User"
        print("Test passed with runtime patching:", response)

# Run the test
test_fetch_data_with_patching()
