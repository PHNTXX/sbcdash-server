import json
import os

def getCPUtemperature():
    res = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline().rstrip()
    return(res)

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)

DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_used = DISK_stats[1]
DISK_free = DISK_stats[2]
DISK_perc = DISK_stats[3]

print(CPU_temp)
print(RAM_free)
print(RAM_used)
print(DISK_free)
print(DISK_used)
print(float(DISK_perc[:-1])/100 )
print(float(RAM_perc)/100)
