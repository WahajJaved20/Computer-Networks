# HTTP / HTTPS Configuration in Cisco Packet Tracer
1. Implement the Topology 

![image](https://user-images.githubusercontent.com/84095994/236680398-9a438c71-c071-45f5-ae5c-dcca5d67afa1.png)

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

![image](https://user-images.githubusercontent.com/84095994/236680733-ed4545b5-685d-486b-9402-e1ead10cada1.png)

3. Assign relevant IPs to both the PCs and the Web Server
4. Assign Gateways to the PCs and the Web Server (The Gateway Address is the interface IP of the router)

5. Configure HTTP Server <br>
Click on the Server -> Services -> HTTP -> Turn HTTP and HTTPS on

![image](https://user-images.githubusercontent.com/84095994/236680784-7c05e508-a76c-4a8f-b45e-5cca4893fb40.png)

## Testing

- Click on PC1 -> Desktop -> Web Browser
- In the Address Bar, type the IP of the Web Server 172.168.0.2

![image](https://user-images.githubusercontent.com/84095994/236681066-1e4f0d9e-7abc-41bf-9c4a-761097a0f2f4.png)

- and thats done, the index.html file from the webserver is loaded.
