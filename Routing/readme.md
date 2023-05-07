# Static Routing Configuration in Cisco Packet Tracer
1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236688941-e8f5aecb-8226-43c6-bb59-152084fa6fd6.png)

2. To interconnect the two routers
- Click on Router
- Physical -> Power off
- Add the HWIC-2T Component
- Turn back on
![image](https://user-images.githubusercontent.com/84095994/236688995-6768216f-d9d3-4b29-ad78-6421d5abdad0.png)
- Connect the Routers using Serial Wires

2. Configure Routers <br>
if we hover over the wire connecting router and the switch, it shows the interface
- In Router 1
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.1 255.255.0.0
no shutdown
interface se0/1/0
ip address 182.168.0.1 255.255.255.0
no shutdown
exit
```
- In Router 2
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 172.168.0.1 255.255.0.0
no shutdown
interface se0/1/0
ip address 182.168.0.2 255.255.255.0
no shutdown
exit
```
once, the router is configured, the connections turn green

![image](https://user-images.githubusercontent.com/84095994/236689171-9a8b37f4-f51a-488f-9ad1-a0c409905726.png)

3. To Configure Static Routing
- Click on Router
```
// ip route <TARGET_NETWORK_ADDRESS> <SUBNET_MASK> <NEXT_HOP_ROUTER_CONNECTED_INTERFACE_PORT>
// in router 1
ip route 192.168.0.0 255.255.0.0 se0/1/0
//in router 2
ip route 172.168.0.0 255.255.0.0 se0/1/0
```
4.  Assign Gateway Addresses and IPs to all PCs

and the static routing is done

## Testing
To Test Connectivity, ping the other PC
- Open Command Prompt in PC0
```
ping 172.168.0.2
```
![image](https://user-images.githubusercontent.com/84095994/236689930-c12f9617-e181-4fa8-a55c-c5a80ee1ac27.png)

The PC is successfully pinged

# RIP(Dynamic) Routing Configuration in Cisco Packet Tracer
1. Implement the Topology using Same serial connections between routers

![image](https://user-images.githubusercontent.com/84095994/236690590-16a85784-b16d-4bdb-bad0-d8932459fe99.png)

2. Configure Routers <br>
if we hover over the wire connecting router and the switch, it shows the interface
- In Router 1
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.1 255.255.255.0
no shutdown
interface se0/1/0
ip address 182.168.0.1 255.255.0.0
no shutdown
exit
```
- In Router 2
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 172.168.0.1 255.255.0.0
no shutdown
interface se0/1/0
ip address 182.168.0.2 255.255.0.0
no shutdown
exit
```
once, the router is configured, the connections turn green

![image](https://user-images.githubusercontent.com/84095994/236690808-3345890c-5cd8-48e2-b2c2-12e847d715b0.png)

3. To Configure RIP Routing
- Click on Router
```
router rip
network <OWN_NETWORK_ADDRESS>
network <SERIAL_CONNECTION_NETWORK_ADDRESS>
// in router 1
network 192.168.0.0
network 182.168.0.0
//in router 2
network 172.168.0.0
network 182.168.0.0
```
4.  Assign Gateway Addresses and IPs to all PCs

and the rip routing is done
## Testing
To Test Connectivity, ping the other PC
- Open Command Prompt in PC0
```
ping 172.168.0.2
```

![image](https://user-images.githubusercontent.com/84095994/236693273-f18f4a0a-79f4-48a6-acba-3c0d5e40aaa8.png)


