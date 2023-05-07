# Subnetting in Cisco Packet Tracer
## Given Task
Let consider an example of subnetting for FAST NUCES. There are 3 departments i.e. CS, EE and<br>
AI.You have to perform subnetting for the allocation of the given requirement
- 90 PCs for CS
- 50 PCs for SE
- 20 PCs for AI<br>
The network address for the given scenario is 196.168.10.0/24. <br>
Implement it on Cisco Packet Tracer
1. Perform Subnetting on Paper
### For CS Department
```
CS 90PCS 7 bits-> 2 ** 7 = 128
network = 192.168.10.0/25
range = 192.168.10.1-126
broadcast = 192.168.10.127
subnet=255.255.255.128 (11111111.11111111.1111111.10000000)
```
### For SE Department
```
SE PCS 50 6 bits
network = 192.168.10.128/26
range = 192.168.10.129-190
broadcast=192.168.10.191
subnet=255.255.255.192
```
 ### For AI Department
 ```
 AI PCS 20 5 bits
network= 192.168.10.192/27
range=192.168.10.193-222
broadcast=192.168.10.223
subnet=255.255.255.224
```
2. Once this subnetting, is done we also need to consider the subnetting for connection between routers
### For CS-SE Router
```
CS-SE Router 2 bits
network = 192.168.10.224/30
range = 192.168.10.225-226
broadcast=192.168.10.227
subnet=255.255.255.252
```
### For CS-AI Router
```
CS-AI Router 2 bits
network = 192.168.10.228/30
range = 192.168.10.229-230
broadcast=192.168.10.231
subnet=255.255.255.252
```
### For AI-SE Router
```
AI-SE Router 2 bits
network = 192.168.10.232/30
range = 192.168.10.233-234
broadcast=192.168.10.235
subnet=255.255.255.252
```

3. Now Assign the PCs their networks based on the subnettings done
The Topology looks like

![image](https://user-images.githubusercontent.com/84095994/236697786-8767b09e-ae0f-4b46-8098-7ff54f0b0d07.png)

4. Add Static Routes
Now for each router add its static Routes

![image](https://user-images.githubusercontent.com/84095994/236697806-ed9decba-0516-4e25-be9f-aa84a86b8c2b.png)

## Testing
To Test Connectivity, ping the other PC
- Open Command Prompt in PC in SE Dept
```
ping 192.168.10.1
```

![image](https://user-images.githubusercontent.com/84095994/236697907-a44a2b0b-2e8e-4c43-ae39-ebb8c5b9d9cf.png)

