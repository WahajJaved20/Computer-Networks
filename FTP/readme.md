# FTP Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236684311-8beda2b0-4a06-434b-b00b-cf00d5de1ad2.png)

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

![image](https://user-images.githubusercontent.com/84095994/236684417-0ec3cd6d-f192-4c40-8c94-a057b2c61a13.png)

3. Assign relevant IPs to both the PCs and the FTP Server
4. Assign Gateways to the PCs and the FTP Server (The Gateway Address is the interface IP of the router)

5. Configure FTP Server <br>
Click on the Server -> Services -> FTP -> Turn FTP on
- In User Setup,
  Username = <OUR_USERNAME> , Password = <PASSWORD>
  Mark the Permissions you want the user to have and click add
  ![image](https://user-images.githubusercontent.com/84095994/236684605-8eda76fc-c4d2-4441-8621-c89d57bad564.png)

The FTP Server is now configured
  
# Testing
 
- Click on PC1 -> Desktop -> Command Prompt
```
// ftp <FTP_SERVER_IP_ADDRESS>
ftp 172.168.0.2
Username: wahaj
Password: wahaj
ftp>
  ```
![image](https://user-images.githubusercontent.com/84095994/236684782-4775b078-300f-4b07-8776-90e37b825774.png)
  
### List the Directory
  ```
  dir
  ```
  ![image](https://user-images.githubusercontent.com/84095994/236684827-c31f973e-735a-4a82-a68a-bd761b6b5040.png)

### Upload a File to the FTP Server
- Go to PC -> Text Editor -> write anything and save -> wahaj.bin
- to upload the file onto the server, go back to the command prompt
```
  //put <FILE_NAME>
  put wahaj.bin
```
  ![image](https://user-images.githubusercontent.com/84095994/236684953-c2b553e2-4acd-4863-93e2-3936e7983ee6.png)
### Downloading a file
  - In the command prompt,
  ```
  // get <FILE_NAME>
  get wahaj.bin
  ```
  ![image](https://user-images.githubusercontent.com/84095994/236684990-bb8fec1b-e943-413c-a7d2-c95d3d7030dd.png)

  
  

 
