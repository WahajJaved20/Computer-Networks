# DNS Configuration in Cisco Packet Tracer
 
The goal of this task is to implement a DNS Server that would redirect requests to the Web Server.

## Types of DNS Records =>
- A Record => name -> IP
- CNAME Record => alias -> name

1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236681533-b98df80e-b1aa-4a4c-8dde-851288b7c809.png)

2. Configure Router <br>
if we hover over the wire connecting router and the switch, it shows the interface
```bash
en
config t
interface gig0/0
// ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.1 255.255.0.0
no shutdown
interface gig0/1
ip address 172.168.0.1 255.255.0.0
no shutdown
exit
```
once, the router is configured, the connections turn green

![image](https://user-images.githubusercontent.com/84095994/236681698-7ccc181d-775f-4afd-b1dc-c9a130a98b29.png)


3.  Assign IPs to all PCs and Servers
4.  Assign Gateway Addresses to all PCs and Servers
5.  Configure HTTP Server<br>
Click on the Server -> Services -> HTTP -> Turn HTTP and HTTPS on

![image](https://user-images.githubusercontent.com/84095994/236680784-7c05e508-a76c-4a8f-b45e-5cca4893fb40.png)

6.  Configure DNS Server <br>
Click on Server -> Services -> DNS -> Turn it on <br>
We will add two types of Records here (A-Record and CNAME-Record)
  - For A Record
  Name = <NAME_FOR_SERVER>, Address = <WEB_SERVER_IP>, click on ADD
  ![image](https://user-images.githubusercontent.com/84095994/236682111-5dc4baee-e48c-492b-942a-4e0bcac71bdd.png)

  - For CNAME Record
  Name = <ALIAS_NAME> Host = <A_RECORD_NAME>
  ![image](https://user-images.githubusercontent.com/84095994/236682130-080157f2-2c42-472c-9543-09d0ad6d4110.png)

7. Assign DNS Server IP Address to all PCs and Servers DNS Server Addresses (even the DNS Server itself)
  ![image](https://user-images.githubusercontent.com/84095994/236682184-0c041ba9-d46c-46ef-b569-a39a7a4e0e62.png)

And thats it for the configuration
  
# Testing
  
- Click on PC1 -> Desktop -> Web Browser
- In the Address Bar, type the name of the Web Server which was listed in the A-Record in DNS Server
  ![image](https://user-images.githubusercontent.com/84095994/236682400-f717d0e6-533c-47fd-911a-36245189038b.png)
- Similarly, type the alias name of the  Web Server which was listed in the CNAME-Record in DNS Server
  ![image](https://user-images.githubusercontent.com/84095994/236682455-ba8deeef-0519-4220-a14e-8807ec55fb32.png)


