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

if __name__ == "__main__":
    server_url = "https://task-management-f8ag.onrender.com/health"
    while True:
        ping_server(server_url)
        time.sleep(60)  # Wait for 1 minute