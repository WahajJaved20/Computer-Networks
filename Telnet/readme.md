# TELNET Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236685411-255d318b-479c-4892-a475-3bbabc7971cb.png)

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
```
once, the router is configured, the connections turn green

![image](https://user-images.githubusercontent.com/84095994/236685539-d594e3cd-ceba-4afe-a534-737bf80d7cf7.png)

3. Configuration of Telnet in any end device
- Open the CLI of the desired device (skip to enable password if configuring router)
```
en
config t
interface vlan 1
ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.5 255.255.0.0 
no shutdown
exit
//enable password <PASSWORD> (password required to enable the end device)
enable password wahaj
line vty 0 15
// password <PASSWORD> (password required to access telnet)
password wahaj
login
exit
```

Thats it for the Configuration

# Testing

- Click on PC1 -> Desktop -> Command Prompt
```
// telnet <TARGET_IP_ADDRESS>
telnet 192.168.0.5
Password: wahaj
Switch> en
Password: wahaj
```
![image](https://user-images.githubusercontent.com/84095994/236686052-1cc4eb41-e369-4b67-8289-d6d7595b6479.png)

and we have access
