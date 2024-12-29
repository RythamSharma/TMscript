import time
import requests

def ping_server(server_url):
    """
    Pings the server and prints the result.

    Args:
        server_url (str): The URL of the server to ping.
    """
    print(f"Pinging {server_url}...")
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print(f"{server_url} is reachable.\n")
        else:
            print(f"{server_url} responded with status code: {response.status_code}.\n")
    except requests.RequestException as e:
        print(f"Failed to reach {server_url}. Error: {e}\n")

if _name_ == "_main_":
    server_url1 = "https://task-management-f8ag.onrender.com/health"
    server_url2 = "https://reviewsystem24.onrender.com/health"
    while True:
        ping_server(server_url1)
        ping_server(server_url2)
        time.sleep(300)  # Wait for 5 minute