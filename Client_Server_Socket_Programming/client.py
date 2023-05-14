import socket
import threading as thread
import tkinter as tk

localhost = ''
port = 0
def submit_port():
    global port
    input_text = text_box_port.get("1.0", "end-1c")  
    print("Input text:", input_text)
    port = int(input_text)
    text_box_port.delete("1.0", "end-1c")
    chat_log.insert(tk.END, 'port number:'+str(port)+"\n")
    text_box_port.config(state=tk.DISABLED)
    submit_button_port.config(state=tk.DISABLED)
def submit_IP():
    global localhost
    input_text = text_box_IP.get("1.0", "end-1c")  
    print("Input text:", input_text)
    localhost = input_text
    text_box_IP.delete("1.0", "end-1c")
    chat_log.insert(tk.END, 'IP:'+localhost+"\n")
    text_box_IP.config(state=tk.DISABLED)
    submit_button_IP.config(state=tk.DISABLED)
def send_message():
    client_message = message_entry.get()
    s.send(client_message.encode())
    message_entry.delete(0,tk.END)
def recv_message():
    while True:    
        msg_recv = s.recv(1024)
        msg_recv = msg_recv.decode("ascii")
        if msg_recv == 'exit':
            break
        chat_log.insert(tk.END, "Server: " + msg_recv + "\n")
    s.close()
    
def connect():
    global s
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    s.connect((localhost,port))
    print("New client created:")
    chat_log.insert(tk.END, "Client connected to 127.0.0.1:"+ str(port) + "\n")
    send_button["state"] = "normal"
    global t2
    t2= thread.Thread(target=recv_message)
    t2.start()

def quit_app():
    root.destroy()
    s.close()
    exit(0)
root = tk.Tk()
root.title("Client Window")

text_box_port = tk.Text(root, height=2, width=10)
text_box_port.pack()

submit_button_port = tk.Button(root, text="Submit Port", command=submit_port)
submit_button_port.pack()

text_box_IP = tk.Text(root, height=2, width=10)
text_box_IP.pack()

submit_button_IP = tk.Button(root, text="Submit IP", command=submit_IP)
submit_button_IP.pack()
# Create connect button
connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

chat_log = tk.Text(root,height=20,width=50)
chat_log.pack()

message_entry = tk.Entry(root, width=50)
message_entry.pack()

# Create send button
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack()
send_button["state"] = "disabled"

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(padx=10, pady=5)


root.mainloop()


