# SSH Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236686891-3287b8ec-19e6-44d5-948f-0a2d67beb648.png)

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

![image](https://user-images.githubusercontent.com/84095994/236686953-45a72913-8dae-43aa-9155-22f8ea82f685.png)

3. Configuration of SSH in any end device
- Open the CLI of the desired device (skip to hostname if configuring router)
```
en
config t
interface vlan 1
ip address <IP_ADDRESS> <SUBNET_MASK>
ip address 192.168.0.5 255.255.0.0 
no shutdown
exit
hostname <HOST_NAME>
ip domain name <DOMAIN_NAME>
crypto key generate rsa
How many bits in the modulus [512]: 1024
ip ssh version 2
line vty 0 15
// password <PASSWORD> (password required to access ssh)
password wahaj
transport input ssh
login local
exit
//enable password <PASSWORD> (password required to enable the end device)
enable password wahaj
// username <OUR_USERNAME> secret <PASSWORD>
username wahaj secret wahaj
exit
```
Thats it for the Configuration

# Testing

- Click on PC1 -> Desktop -> Command Prompt
```
// ssh -l <OUR_USERNAME> <TARGET_IP_ADDRESS>
ssh -l wahaj 192.168.0.5
Password: wahaj
s1> en
Password: wahaj
s1#
```
![image](https://user-images.githubusercontent.com/84095994/236687423-b524dca4-15a5-4e25-8c86-bdf3ee1cb6a2.png)

and we have access via SSH

