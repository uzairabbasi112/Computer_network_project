# 💬 Computer Network Project: Chatting System 💬  

This project implements a **client-server** based **chatting system**, where:  
- 🖥️ **One server (Admin)** receives messages  
- 👥 **Multiple clients** can connect and send messages  

Each client uses the same **client file** to communicate with the **server**.  

---

## 📂 Project Overview  

- **Files Included:**  
  - `server.py` → Runs the server and listens for client messages  
  - `client.py` → Used by multiple clients to send messages  

- **How It Works:**  
  1. The **server** is started first.  
  2. It displays the **IP address** where it is running.  
  3. Clients need to **update** their `SERVER_IP` in `client.py` to match the server’s IP.  
  4. Once connected, clients can send messages.  
  5. The **server displays** messages along with the **client’s name and IP address**.  

---

## ⚙️ Installation and Setup  

### 1️⃣ **Run the Server**  
Start the server by executing:  
```sh
python server.py
