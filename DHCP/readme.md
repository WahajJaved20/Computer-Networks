# DHCP Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236687659-98b2d171-a63e-4c76-9bb7-93a96e35a8ef.png)

2. Configure Router <br>
if we hover over the wire connecting router and the switch, it shows the interface
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.1 255.255.0.0
no shutdown
exit
interface gig0/1
ip address 172.168.0.1 255.255.0.0
no shutdown
exit
```
once, the router is configured, the connections turn green

![image](https://user-images.githubusercontent.com/84095994/236687841-637da67e-620a-4e92-bf77-f10032d71c52.png)

3. Assign relevant IPs to the Server
4. Assign Gateways to the Server (The Gateway Address is the interface IP of the router)

5. Configure HTTP Server <br>
Click on the Server -> Services -> HTTP -> Turn HTTP and HTTPS on

![image](https://user-images.githubusercontent.com/84095994/236687906-67672cac-7f19-42a4-b7fe-bc5f7dcb754f.png)


6.  Configure DNS Server <br>
Click on Server -> Services -> DNS -> Turn it on <br>
  - For A Record
  Name = <NAME_FOR_SERVER>, Address = <WEB_SERVER_IP>, click on ADD
  ![image](https://user-images.githubusercontent.com/84095994/236687995-cd68e9ce-52a7-46c9-bf95-cc93ad8c8356.png)

7. Configure DHCP Server <br>
Click on Server -> Services -> DHCP -> Turn it on <br>
- Pool Name = <POOL_NAME>
- Default Gateway = <ROUTER_IP_ADDRESS>
- DNS Server = <DNS_SERVER_IP_ADDRESS>
- start IP Address = <Starting for the Network>
- Subnet Mask = <SUBNET_MASK>
  click on add, repeat it for the other network as well
  ![image](https://user-images.githubusercontent.com/84095994/236688240-3d4d9eee-b5a8-4514-94bb-9ce3ca87a9d8.png)

8. Configure Router for DHCP Support (we will exclude all the IPs that we need to be static like server and router)
  Open Router CLI
```
Router>en
Router#config t
Router(config)#ip dhcp pool leftPool
Router(dhcp-config)#network 192.168.0.0 255.255.0.0
Router(dhcp-config)#default-router 192.168.0.1
Router(dhcp-config)#dns-server 172.168.0.2
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 192.168.0.1
Router(config)# ip dhcp pool rightPool
Router(dhcp-config)#network 172.168.0.0 255.255.0.0
Router(dhcp-config)#default-router 172.168.0.1
Router(dhcp-config)#dns-server 172.168.0.2
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 172.168.0.1
Router(config)#ip dhcp excluded-address 172.168.0.2
Router(config)#exit
```

  Thats is for the configuration

# Testing
  
- Click on PC1 -> Desktop -> IP Configuration
- Select DHCP and the IP will be automatically assigned
  ![image](https://user-images.githubusercontent.com/84095994/236688615-7fd5ba60-dcfe-4f59-a0b4-9448511b523f.png)

  
