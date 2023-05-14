import socket
import time
# defining the constants
END_TRANSMISSION_FLAG = "EOF"
PACKET_SIZE = 1024
TIMEOUT = 5
DATA_TO_SEND = "Immortal temptation Takes over my mind, condemned Falling weak on my knees Summon the strength of mayhem I am the storm that is approaching Provoking black clouds in isolation I am reclaimer of my name Born in flames, I have been blessed My family crest is a demon of death Forsakened, I am awakened A phoenix's ash in dark divine Descending misery Destiny chasing time Inherit the nightmare, surrounded by fate Can't run away Keep walking the line, between the light Led astray Through vacant halls I won't surrender The truth revealed in eyes of ember We fight through fire and ice forever Two souls once lost, and now they remember I am the storm that is approaching Provoking black clouds in isolation I am reclaimer of my name Born in flames, I have been blessed My family crest is a demon of death Forsakened, I am awakened A phoenix's ash in dark divine Descending misery Destiny chasing time Disappear into the night Lost shadows left behind Obsession's pulling me Fading, I've come to take what's mine Lurking in the shadows under veil of night Constellations of blood pirouette Dancing through the graves of those who stand at my feet Dreams of the black throne I keep on repeat A derelict of dark, summoned from the ashes The puppet master congregates all the masses Pulling strings, twisting minds as blades hit You want this power? Then come try and take it Beyond the tree, fire burns Secret love, bloodline yearns Dark minds embrace, crimson joy Does your dim heart heal or destroy? Bury the light deep within Cast aside, there's no coming home We're burning chaos in the wind Drifting in the ocean all alone"

# creating the TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# setting the reciever address and port number
recieverAddress = ('localhost', 9000)

# binding the socket to the reciever address and port number
sock.connect(recieverAddress)
print("Connected to the reciever")
print("-----------------------------------")
# converting data into packets
def makePackets(data):
    packets = []
    currentSequenceNumber = 0
    for i in range(0, len(data), PACKET_SIZE):
        # to corrupt a packet, uncomment the following line and comment the next line
        # packets.append(str(currentSequenceNumber) + data[i:i+PACKET_SIZE])
        packets.append(str(currentSequenceNumber) + data[i-1 if i > 0 else i:i+PACKET_SIZE-1])
        currentSequenceNumber = 0 if currentSequenceNumber == 1 else 1
    return packets

packets = makePackets(DATA_TO_SEND)

# packet number keeps track of the packet to be sent
packetNumber = 0
# expectedAcknowledgmentNumber keeps track of the expected acknowledgement number
expectedAcknowledgmentNumber = 0
# a timer array to keep each packets timeout in consideration
timers = [None for i in range(len(packets))]

while True:
    # if a packet can be sent, send it and start its timer
    if packetNumber < len(packets):
        if timers[packetNumber] is None:
            timers[packetNumber] = time.time()
            sock.send(packets[packetNumber].encode())
            print("Packet sent: " + packets[packetNumber][1:]) 
    # set the timeout for the socket
    sock.settimeout(TIMEOUT)
    try:
        # try to recieve the acknowledgement
        acknowledgementNumber = sock.recv(PACKET_SIZE).decode()
        print("-----------------------------------")
        print("Acknowledgement received: " + acknowledgementNumber)
        print("-----------------------------------")
        # if the ack number is the same as the expected number, then the packet was received successfully
        # else the ack is discarded
        if acknowledgementNumber == END_TRANSMISSION_FLAG:
            print("End of transmission flag received")
            break
        if acknowledgementNumber == str(expectedAcknowledgmentNumber):
            expectedAcknowledgmentNumber = 0 if expectedAcknowledgmentNumber == 1 else 1
            timers[packetNumber] = None
            packetNumber += 1
    # if a timeout occurs, resent the packet
    except socket.timeout:
        timers[packetNumber] = time.time()
        sock.send(packets[packetNumber].encode())
        print("-----------------------------------")
        print("Socket Timeout")
        print("-----------------------------------")
        print("Packet resent: " + packets[packetNumber])
    # if all the packets are sent, break the loop
    if packetNumber == len(packets):
        print("Sending the final transmission message")
        sock.send(END_TRANSMISSION_FLAG.encode())
    
sock.close()