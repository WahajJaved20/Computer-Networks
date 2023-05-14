# Problem Statement

Develop a simple “Chat Messenger” that is connection oriented (i.e. it uses TCP) and that consists of a Client and
a Server Program.
1) The Server runs first and waits for some client to contact it.
2) Client Program starts and connects to the server.
3) Client-Server sends and receives messages.
An Example for each step is shown below.
Step 1) A Server should listen to a specific Port

Step 2) A Client should specify IP Address and Port of the Server.

Step 3) Both Programs can send/receive messages successfully through socket (Port). If you are running
both programs on the same system then server IP can be ‘127.0.0.1’ while you can also use your private IP in
place of ‘localhost’ IP.

Both the programs should be able to send and receive messages simultaneously and for this purpose you can use
threads. Each Program will have one “Input Thread” and one “Output Thread”. Input Thread waits for the input that
may come from the other program while Output Thread sends the typed message to the other program using
sockets.
