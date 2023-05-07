# NAT Configuration in Cisco Packet Tracer
## Static NAT => one private -> one public (one-to-one mapping)
## Dynamic NAT => pool of public IPs -> private IPs
## PAT (Port Address Translation) => multiple private IPs -> Single Public IPs
1. Implement the Topology

![image](https://user-images.githubusercontent.com/84095994/236700172-ee963c3d-2b2c-48aa-9252-6d9dad1995a3.png)

2. Configure Routers

- For Router 1
```
Router>en
Router#config t
Router(config)#int fa0/0
Router(config-if)#ip address 192.168.10.1 255.255.255.0
Router(config-if)#no shutdown
Router(config-if)#interface Serial0/3/0
Router(config-if)#ip address 20.0.0.1 255.0.0.0
Router(config-if)#no shutdown
```
- For Router 2
```
Router>en
Router#config t
Router(config)#int fa0/0
Router(config-if)#ip address 10.0.0.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#int se0/3/0
Router(config-if)#ip address 20.0.0.2 255.0.0.0
Router(config-if)#no shutdown
```

3. Configure Static NAT for Router 1
```
// ip nate inside source static <PRIVATE_IP> <PUBLIC_IP>
Router(config)#ip nat inside source static 192.168.10.2 20.0.0.3
Router(config)#ip nat inside source static 192.168.10.3 20.0.0.4
Router(config)#ip nat inside source static 192.168.10.4 20.0.0.5
Router(config)#interface se0/3/0
Router(config-if)#ip nat outside
Router(config-if)#interface fa0/0
Router(config-if)#ip nat inside
```
- now we need to add a static route from router 1 to 2
we used 0.0.0.0 because we dont know what IP will be coming to us 
```
Router(config)#ip route 0.0.0.0 0.0.0.0 se0/3/0
```

If a packet is sent and observed, the IP address can be seen as being changed to the public

![image](https://user-images.githubusercontent.com/84095994/236700614-f524923e-0efc-4e1e-ad9c-ebde13a8f8eb.png)


4. Configure Dynamic NAT for Router 2
```
// ip nat pool <name> <public IP start> <public IP end> netmask <subnetmask>
Router(config)#ip nat pool MY_POOL 20.0.0.6 20.0.0.20 netmask 255.0.0.0
// access-list 1 permit <internal network address> <wildcard subnet>
Router(config)#access-list 1 permit 10.0.0.0 0.255.255.255
// ip nat inside source list 1 pool <name>
Router(config)#ip nat inside source list 1 pool MY_POOL
Router(config)#interface se0/3/0
Router(config-if)#ip nat outside
Router(config-if)#interface fa0/0
Router(config-if)#ip nat inside
```

If we ping the private IP in the other network, the reply gets translated by the public IP

![image](https://user-images.githubusercontent.com/84095994/236700769-d0af0c99-599e-4efd-8525-97a7320d8cfb.png)

### For PAT
```
access list 1 permit <PRIVATE_IP_NETWORK_ADDRESS> <WILDCARD_MASK>
ip nat inside source list 1 interface <PORT> overload
interface <PORT>
ip nat <INSIDE/OUTSIDE>
```
