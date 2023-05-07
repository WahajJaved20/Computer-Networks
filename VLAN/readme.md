# VLAN Configuration in Cisco Packet Tracer
1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236698177-baaf1206-c31b-49e9-ab16-aec3975b4fcf.png)

2. Assign Switches as Trunk or Access Links
In Each side of the router, we will have one pc for each of the VLANs (1 for CS,1 for EE, 1 for ACD)
- Trunk Link => both devices in the connection are VLAN aware (routing devices are)
- Access Link => VLAN unaware device with VLAN aware bridge(switch/router)
To Configure the switches,
```
// vlan <VLAN_NUMBER>
// name <NAME_FOR_VLAN>
Switch(config)#vlan 10
Switch(config-vlan)#name EE
Switch(config-vlan)#vlan 20
Switch(config-vlan)#name CS
Switch(config-vlan)#vlan 30
Switch(config-vlan)#name ACD
```
Now, we have to decide which port of the switch will belong to which VLAN
```
// switchport mode <ACCESS/TRUNK>
// If in access mode, 
// switchport access vlan <VLAN_NUMBER>
Switch(config)#interface fa0/1
Switch(config-if)#switchport mode trunk
Switch(config-if)#interface fa0/2
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 10
Switch(config-if)#interface fa0/3
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 20
Switch(config-if)#interface fa0/4
Switch(config-if)#switchport mode access
Switch(config-if)#switchport access vlan 30
Switch(config-if)#exit
```
3. Router Configuration
```
Router(config)#interface gig0/0
Router(config-if)#interface gig0/0.10
Router(config-subif)#encapsulation dot1q 10
Router(config-subif)#ip address 10.0.0.1 255.0.0.0
Router(config-subif)#interface gig0/0.20
Router(config-subif)#encapsulation dot1q 20
Router(config-subif)#ip address 20.0.0.1 255.0.0.0
Router(config-subif)#interface gig0/0.30
Router(config-subif)#encapsulation dot1q 30
Router(config-subif)#ip address 30.0.0.1 255.0.0.0
Router(config-subif)#exit
Router(config)#interface gig0/0
Router(config-if)#no shutdown
```
3. A Basic Representation of IPs and Trunk and Access Links
![image](https://user-images.githubusercontent.com/84095994/236699066-1b542565-9792-455e-b12c-a5835d3cd08e.png)

## Testing
To Test Connectivity, ping the other PC from 10 vlan
- Open Command Prompt in PC0
```
ping 10.0.0.3
ping 20.0.0.3 (to make sure that other VLANs are not accessible)
```
![image](https://user-images.githubusercontent.com/84095994/236699109-5317fa0b-7cb0-4056-b659-8c8d3d03f96e.png)
