# ACL Configuration in Cisco Packet Tracer
### Inbound ACL => packets processed then routed
### Outbound ACL => packets routed then processed
### Numbered ACL => Once created, cannot delete => deleting removes the whole ACL
### Named ACL => deletable and readable and modifiable
1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236702495-ab94fbd9-51ca-44b8-8b2b-5d53f487bae3.png)

2. Configure Router
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

![image](https://user-images.githubusercontent.com/84095994/236702659-25c37a3e-36b5-4348-924c-cb88359b00ea.png)

3. Assign relevant IPs to both the PCs and the Web Server
4. Assign Gateways to the PCs and the Web Server (The Gateway Address is the interface IP of the router)

5. Configure HTTP Server <br>
Click on the Server -> Services -> HTTP -> Turn HTTP and HTTPS on

![image](https://user-images.githubusercontent.com/84095994/236702668-39f81d12-0f33-4587-aac4-70ce1e9165e6.png)

6. Create Standard ACL to only allow Management PC (192.168.0.2) to access the router
- Configuration of Telnet in router
- Open the CLI
```
en
config t
//enable password <PASSWORD> (password required to enable the end device)
enable password wahaj
line vty 0 15
// password <PASSWORD> (password required to access telnet)
password wahaj
login
exit
```
- For Standard ACL 
```
// ip access-list standard <ACL_NAME>
Router(config)#ip access-list standard TEL
// permit / deny <any> the order of statements matters as first is executed first
Router(config-std-nacl)#permit 192.168.0.2
Router(config-std-nacl)#deny any
Router(config-std-nacl)#exit
Router(config)#interface gig0/0
// ip access-group <NAME> <IN/OUT>
Router(config-if)#ip access-group TEL in
```
- If we Telnet from Management PC (success)

![image](https://user-images.githubusercontent.com/84095994/236702976-9e8f45f4-aabb-4430-a0bc-12fa42751cc1.png)

- If we try from the User PC (fail)

![image](https://user-images.githubusercontent.com/84095994/236703001-ed388bee-f952-4b18-89ff-439bef5c915c.png)

7. Create an Extended ACL to only allow Web Services from the Server and Block Everything else
```
//ip access-list extended <ACL_NAME>
Router(config)#ip access-list extended allowWeb
// permit/deny <TCP/UDP> <SOURCE_IP_ADDRESS> <WILDCARD_MASK> host <DESTINATION_ADDRESS> eq <PORT_NUMBER_OF_SERVICE>
Router(config-ext-nacl)#permit tcp 192.168.0.0 0.0.255.255 host 172.168.0.2 eq 80
Router(config-ext-nacl)#deny ip 192.168.0.0 0.0.255.255 host 172.168.0.2
Router(config-ext-nacl)#exit
Router(config)#interface gig0/0
Router(config-if)#ip access-group allowWeb in
```

- delete the previous ACL in case extended clashes due to statements
- try to perform http query using pc (success)

![image](https://user-images.githubusercontent.com/84095994/236703750-bd14d811-eb92-419a-a343-0f6e62057729.png)

-if we try to ftp, it is denied

![image](https://user-images.githubusercontent.com/84095994/236703770-bb083f65-fb2f-43c8-8c3e-26240fc02467.png)




