import socket

HOST = '100.83.170.97'  # Must match broker's Tailscale IP
PORT = 1234

# Create a TCP socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    # Identify as a subscriber (critical first message)
    s.sendall(b"subscriber")
    print("Subscribed to updates...")

    while True:
        data = s.recv(1024)  # Receive data in chunks
        if not data:
            print("Server closed the connection.")
            break
        print(f"Received: {data.decode().strip()}")

except ConnectionRefusedError:
    print(f"Could not connect to {HOST}:{PORT}")
except Exception as e:
    print(f"Error: {e}")
finally:
    s.close()
