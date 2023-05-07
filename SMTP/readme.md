# SMTP Server Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236682731-4936a65d-3b34-4411-88bb-cdc005b4ddc7.png)

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

![image](https://user-images.githubusercontent.com/84095994/236682884-a2d3a158-35e8-43fc-b538-16dc61b6e10a.png)

3. Assign relevant IPs to both the PCs and the Mail Server
4. Assign Gateways to the PCs and the Mail Server (The Gateway Address is the interface IP of the router)

5. Configure SMTP Server <br>
Click on the Server -> Services -> EMAIL -> Turn SMTP and POP3 On <br>
- Domain Name = <domain>.com, Press Set
- Add users by adding their usernames and passwords and clicking on +
  ![image](https://user-images.githubusercontent.com/84095994/236683282-26321ef3-272e-45d9-a07c-db84b04f64bb.png)

6. Click on PC0 -> Desktop -> Email
  - Your name = <OUR_NAME>
  - Email Address = <username>@<domain>.com
  - Incoming Mail Server = Outgoing Mail Server = <MAIL_SERVER_IP_ADDRESS>
  - Enter the username and password in the Logon Information, press Save
  ![image](https://user-images.githubusercontent.com/84095994/236683444-a354e0b1-6bbb-47b8-adf6-0ec67c98ec93.png)
  
7. Repeat the Same Process for all PCs
SMTP configuration is done

# Testing
- Click on PC0 -> Desktop -> Email
![image](https://user-images.githubusercontent.com/84095994/236683503-57897955-a837-4c60-8096-f49dfc3d48c9.png)

- Click on Compose and write the recipient and the message and press Send
  ![image](https://user-images.githubusercontent.com/84095994/236683694-c832b41b-8bdf-4125-a91d-93c2110c8a4c.png)

- This line at the bottom verifies that the email was sent
  ![image](https://user-images.githubusercontent.com/84095994/236683701-916b8cee-9f0c-41fe-ae8c-d9497d4c58f2.png)

- Now, go the recipient PC -> Desktop -> Email
- Click on Recieve
  ![image](https://user-images.githubusercontent.com/84095994/236683720-9aaaa25b-4aed-4737-9241-6358014e87b5.png)
- And the mail is recieved along with the success message
  

  
