import socket
import threading
import tkinter as tk

# Server configuration
HOST = '0.0.0.0'  # Bind to all available network interfaces
PORT = 5555
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

# Get IP address of the current PC
def get_ip_address():
    try:
        # Create a temporary socket
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        ip_address = temp_socket.getsockname()[0]
        temp_socket.close()
        return ip_address
    except socket.error:
        return "Could not retrieve IP address"

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Counter for message sequence number
message_counter = 0

# Function to handle client connections
def handle_client(conn, addr):
    global message_counter
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive message from client
        msg = conn.recv(1024).decode(FORMAT)
        if msg == "exit":
            connected = False
        print(f"[{addr}] {msg}")

        # Broadcast message to all clients
        for client in clients:
            if client != conn:
                client.send(msg.encode(FORMAT))

        # Display message in server GUI
        server_gui_display(addr, msg, message_counter)
        message_counter += 1

    conn.close()

# List to store client connections
clients = []

# Start listening for incoming connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        # Accept new connection
        conn, addr = server.accept()
        clients.append(conn)

        # Start a new thread to handle client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# Function to display messages in server GUI
def server_gui_display(addr, msg, message_number):
    server_display.config(state=tk.NORMAL)
    name = msg.split(":")[0]
    ip = addr[0]
    message = msg.split(":")[1].strip()
    server_display.insert(tk.END, f"{message_number}.\t {name}:\t\t {ip}\t\t{message}\n", "bold")
    server_display.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
    server_display.config(state=tk.DISABLED)

# Create GUI for server
server_root = tk.Tk()
server_root.title("Chat Server")

# Get and display the IP address as the heading
ip_address = get_ip_address()
ip_label = tk.Label(server_root, text=f"Server IP Address: {ip_address}", font=("Helvetica", 12, "bold"))
ip_label.pack()

# Server message display
server_display = tk.Text(server_root, height=20, width=80)
server_display.pack()

# Start the server
start_thread = threading.Thread(target=start)
start_thread.start()

# Run the server GUI
server_root.mainloop()
