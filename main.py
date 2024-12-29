import os
import time

def ping_server(server_ip):
    """
    Pings the server and prints the result.

    Args:
        server_ip (str): The IP address of the server to ping.
    """
    print(f"Pinging {server_ip}...")
    response = os.system(f"ping -c 1 {server_ip}" if os.name != 'nt' else f"ping -n 1 {server_ip}")

    if response == 0:
        print(f"{server_ip} is reachable.\n")
    else:
        print(f"Failed to reach {server_ip}.\n")

if __name__ == "__main__":
    server_ip = "15.206.147.95"
    while True:
        ping_server(server_ip)
        time.sleep(60)  # Wait for 1 minute