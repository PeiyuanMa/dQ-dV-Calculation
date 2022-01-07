#!/usr/bin/env python
# coding: utf-8

# # This script aims at calculating dQ/dV curve from Capacity-Voltage data.
# 
# # Need Capacity-Voltage data in two columns as input
# # Output Voltage-dQ/dV data in two columns

# In[11]:


import copy
import matplotlib.pyplot as plt


# In[12]:


# file reading
file = open("E4F-1stlithiation.csv","r")
data = file.readlines()
file.close()

data_ori = []
Cap = []
Vol = []
for i in range (len(data)):
    data_ori.append(data[i].split(","))
    xx_ori, yy_ori = data_ori[i]
    y_ori = yy_ori.replace("\n","")
    x_ori = xx_ori.replace("ï»¿","")
    Cap.append(float(x_ori))
    Vol.append(float(y_ori))
        
plt.plot(Cap, Vol)


# In[13]:


#calculate dQ/dV
interval = 0.002 # Intervals between 0.001 V and 0.003 V are used for different files to acquire appreciable signal-to-noise ratio 
dQdV = []
newV = []
tempV = Vol[0]
tempQ = Cap[0]
for i in range (len(Cap)):
    if (Vol[i]-tempV) < -interval:
        dQ = Cap[i] - tempQ
        dV = Vol[i] - tempV
        dQdV.append(dQ/dV)
        newV.append((Vol[i]+tempV)/2)
        tempV = Vol[i]
        tempQ = Cap[i]
        
plt.plot(newV, dQdV)


# In[14]:


#write output file
out = open("E4F-1stlithiation-newdQdV.txt","w")
for i in range (len(dQdV)):
    out.write(f"{newV[i]}, {dQdV[i]}\n")
    
out.close()

