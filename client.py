import socket
import threading
import tkinter as tk

# Server configuration
SERVER_IP = '192.168.10.12'  # Replace with the server's IP address
SERVER_PORT = 5555
ADDR = (SERVER_IP, SERVER_PORT)
FORMAT = 'utf-8'

# Global variable to store the user's name
user_name = None

# Function to receive messages from server
def receive():
    connected = True
    while connected:
        try:
            # Receive message from server
            msg = client.recv(1024).decode(FORMAT)
            print(msg)
        except:
            print("[CONNECTION CLOSED] Connection to server closed.")
            connected = False

# Function to send message to server
def send():
    global user_name  # Access the global user_name variable
    if user_name is None:  # If the name is not set yet
        user_name = name_entry.get()  # Set the name
        name_entry.config(state='disabled')  # Lock the name entry
    msg = msg_entry.get()
    if msg:
        client.send(f"{user_name}: {msg}".encode(FORMAT))
        msg_entry.delete(0, tk.END)

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(ADDR)

# Create GUI
root = tk.Tk()
root.title("Chat Client")
root.geometry("400x300")  # Set the initial size of the window

# Configure grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Name entry
name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

# Message entry
msg_label = tk.Label(root, text="Enter message:")
msg_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
msg_entry = tk.Entry(root)
msg_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

# Send button
send_btn = tk.Button(root, text="Send", command=send)
send_btn.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Run GUI
root.mainloop()

client.close()
