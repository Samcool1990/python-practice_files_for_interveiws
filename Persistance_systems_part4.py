import threading

list1 = [1, 5, 6, 9, 7, 4]

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorials(chunk):
    results = []
    for num in chunk:
        results.append(factorial(num))
    return results

def main():
    num_threads = 2  # Adjust the number of threads as needed
    chunk_size = len(list1) // num_threads
    threads = []

    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_threads - 1 else len(list1)
        thread = threading.Thread(target=calculate_factorials, args=(list1[start_idx:end_idx],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()


#SOrt by string element size

A = ["to", "hello", "i", "six"]
Output = ["i","to", "six", "hello"]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        if len(A[i]) > len(A[j]):
            A[i], A[j] = A[j], A[i]

print(A)



# How to Deploy django linux server
'''To deploy a Django application on a Linux server, you'll need to follow several steps. 
Since you're a Backend Engineer, I'll provide you with a professional and practical guide:

Prepare Your Server:
Choose a Linux distribution (e.g., Ubuntu, CentOS) and set up a server with the necessary resources 
(CPU, RAM, storage).
Ensure you have SSH access to the server.
# Update System Packages:
# sql
# Copy code
# sudo apt update
# sudo apt upgrade
# Install Required Software:

# Install Python, pip, and virtualenv:
# Copy code
# sudo apt install python3 python3-pip python3-venv


# Create a Virtual Environment:

# Navigate to your project directory and create a virtual environment:
# bash
# Copy code
# python3 -m venv myenv
# source myenv/bin/activate

Clone Your Django Project:

Use git or upload your Django project to the server.
Install Project Dependencies:

While in the virtual environment, install the necessary packages:
Copy code
pip install -r requirements.txt
Configure Django Settings:

Update your Django settings for production, including setting DEBUG = False, configuring ALLOWED_HOSTS, 
and adding the server's IP or domain.
Collect Static Files:

Copy code
python manage.py collectstatic
Set Up a Web Server:

You can use Gunicorn or uWSGI to serve your Django application. For example, using Gunicorn:
bash
Copy code
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
Set Up a Reverse Proxy:

Use a web server like Nginx or Apache as a reverse proxy to handle incoming requests and forward them to 
Gunicorn or uWSGI.
Configure SSL (Optional but Recommended):
Set up SSL certificates using Let's Encrypt for secure HTTPS connections.
Start and Enable Services:
Start and enable the services to ensure your Django application runs on server boot.
Monitor and Maintain:
Set up monitoring, logging, and regular maintenance tasks like backups and security updates.
Remember to replace myenv, myproject, and other placeholders with your actual project names and paths. 
Additionally, adapt the instructions based on your specific project requirements and server setup. If you 
have any specific questions or encounter any issues during the process, feel free to ask for further 
assistance.'''

