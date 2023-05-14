import socket

def checkCorruptedPacket(packet):
    return packet[0].isdigit() == False
# constants
PACKET_SIZE = 1024
END_TRANSMISSION_FLAG = "EOF"
# creating the TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the sender port number
sock.bind(('localhost', 9000))

# Listen for incoming connections
sock.listen(1)

# Accept a connection
conn, addr = sock.accept()
print("-----------------------------------")
print("Connected to Sender")
print("Sender Address: " + str(addr))
# can only be 0 and 1
expectedSequenceNumber = 0
completeMessage = ""
while True:
    # recieve a packet 
    packet = conn.recv(PACKET_SIZE)
    data = packet.decode()
    if data == END_TRANSMISSION_FLAG:
        print("-----------------------------------")
        print("End of transmission flag received")
        print("Sending the final transmission message")
        print("-----------------------------------")
        conn.send(END_TRANSMISSION_FLAG.encode())
        break
    if checkCorruptedPacket(data):
        conn.send(str(0 if expectedSequenceNumber == 1 else 0).encode())
        print("Corrupted packet recieved, discarding and sending previous ack: " + str(0 if expectedSequenceNumber == 1 else 0))
        continue
    sequenceNumber = (packet.decode())[0]
    data = (packet.decode())
    # if the sequence number is the same as the expected sequence number, then the packet is received successfully
    if int(sequenceNumber) == int(expectedSequenceNumber):
        # send an acknowledgement
        print("-------------------------------------------------------------")
        print("Packet received successfully with sequence number: " + str(sequenceNumber))
        print("-------------------------------------------------------------")
        conn.send(str(expectedSequenceNumber).encode())
        print("Packet received: " + data[1:])
        completeMessage += data[1:]
        # change the expected sequence number
        expectedSequenceNumber = 0 if expectedSequenceNumber == 1 else 1
    else:
        # if the sequence number is not the same as the expected sequence number, then the packet is discarded and previous ack is sent
        conn.send(str(0 if expectedSequenceNumber == 1 else 0).encode())
        print("Old packet recieved, discarding and sending previous ack: " + str(0 if expectedSequenceNumber == 1 else 0))

print("Complete Message: " + completeMessage)
conn.close()
sock.close()