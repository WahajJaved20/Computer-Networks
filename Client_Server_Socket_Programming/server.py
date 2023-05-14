import socket
import threading as thread
import tkinter as tk

localhost = '127.0.0.1'
port = 0
def submit_port():
    global port
    input_text = text_box_port.get("1.0", "end-1c")  
    print("Input text:", input_text)
    port = int(input_text)
    text_box_port.delete("1.0", "end-1c")
    submit_button_port.config(state=tk.DISABLED)
    chat_log.insert(tk.END, 'IP:'+localhost+"\n")
    chat_log.insert(tk.END, 'port number:'+str(port)+"\n")
    text_box_port.config(state=tk.DISABLED)
def send_message():
    
    msg_send = message_entry1.get() 
    client_sockets.send(msg_send.encode("ascii"))
    message_entry1.delete(0,tk.END)

def recv_message():
    while True:
        msg_recv = client_sockets.recv(1024)
        msg_recv = msg_recv.decode("ascii")
        if msg_recv == 'quit':
            send_button["state"] = "normal"
            break
        chat_log.insert(tk.END, "Client: " + msg_recv + "\n")
        

    client_sockets.close()

def connect():
    global client_sockets
    client_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sockets.bind((localhost,port))
    client_sockets.listen(5)
    client_sockets,addr=client_sockets.accept()
    chat_log.insert(tk.END, "Server connected to 127.0.0.1:"+ str(port) + "\n")
    send_button["state"] = "normal"
    t2 = thread.Thread(target=recv_message)
    t2.start()
def quit_app():
    root.destroy()
    client_sockets.close()
    exit(0)
# Create main window
root = tk.Tk()
root.title("Server Window")

text = tk.Label(text = "Server IP Address: " + str(localhost))
text.place(height=3,width=10)
text.pack()

text_box_port = tk.Text(root, height=2, width=10)
text_box_port.pack()

submit_button_port = tk.Button(root, text="Submit Port", command=submit_port)
submit_button_port.pack()

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()


chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()


message_entry1 = tk.Entry(root, width=50)
message_entry1.pack()

send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack()
send_button["state"] = "disabled"
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(padx=10, pady=5)

root.mainloop()
