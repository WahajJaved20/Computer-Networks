# Wireless Routing Configuration in Cisco Packet Tracer
1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236699448-1a1bdae5-607e-46c4-91d4-9c860c7d3338.png)

2. Setup PCs with WMP 300N Module(They dont have WIFI modules built in)

![image](https://user-images.githubusercontent.com/84095994/236699492-403f6177-63b1-4436-9e52-fdafc2203f50.png)

3. Wireless Router Configuration
- Click on Router -> GUI -> Scroll to Network Settings and see if DHCP is turned on \

![image](https://user-images.githubusercontent.com/84095994/236699557-044ac36d-03e3-4ff3-be26-c9b22d901bfc.png)

- Then go to wireless, change the SSID to your name

![image](https://user-images.githubusercontent.com/84095994/236699585-8c5c8943-cb96-4e0a-a52a-a1f012fda2b4.png)

- Then go to Wireless Security
Change the Security Mode to WEP and enter any passphrase

![image](https://user-images.githubusercontent.com/84095994/236699606-6ee07328-bccc-4b99-8b7a-3f01adf3dbd5.png)

scroll to the bottom and press save settings.

4. PC to WIFI Connection Configuration
- go to PC -> Config -> Wireless0
- Enter the SSID as entered in router
- In Authentication, select WEP and enter the passphrase

![image](https://user-images.githubusercontent.com/84095994/236699726-220469a5-adcf-4032-bf14-7adb2bba4d62.png)

- Then Desktop -> PC Wireless -> Connect
- Select the WIFI connection and press connect

![image](https://user-images.githubusercontent.com/84095994/236699717-93ab8e08-fb30-40c3-837d-38f97a001245.png)

- Enter the Key and Press Connect

![image](https://user-images.githubusercontent.com/84095994/236699743-8fc2c774-e736-412f-b151-7841476256b4.png)

- go to Link Information and its connected

![image](https://user-images.githubusercontent.com/84095994/236699770-4b065cf0-61e8-48a2-a27e-1a27e30abf1b.png)

4. The Topology shows the Wifi connections built

![image](https://user-images.githubusercontent.com/84095994/236699786-603a02bf-6850-480a-9c4c-328739ec5015.png)

5. LAN Configurations
- Click on the Wired Router
- Configure it and assign a different network IP address

![image](https://user-images.githubusercontent.com/84095994/236699852-e1cb68ec-a3fc-43d4-9198-272712ba7976.png)

- Now Click on Wireless Router -> GUI
- In the Internet Setup, select Static IP from the dropdown
- In the internet IP address, enter the IP from the network of the wired router
- the gateway is the address of the wired router

![image](https://user-images.githubusercontent.com/84095994/236699909-157ffe39-6425-4e12-9257-941ce6130d58.png)

- Finally in the PCs and Servers, assign Static IPs from the network of the wired router

and thats it for the wireless and LAN configuration.

## Testing
To Test Connectivity, ping the other PC
- Open Command Prompt in WIFI connected PC and Enter IP of wired PC
```
ping 2.8.0.3
```

![image](https://user-images.githubusercontent.com/84095994/236699995-ec0451ea-6806-4009-92dd-1c8b4ad667d1.png)

