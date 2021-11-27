import psutil
import platform
from datetime import datetime

def getDiskSize(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
def getPecentageFormat(percent):
    if percent < 10:
        return f"{percent}% "
    return f"{percent}%"

print("-"*40, "Disk Info", "-"*40)
partitions = psutil.disk_partitions()

for partition in partitions:
    print(f"----- Disk: {partition.device} -----")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        print('Not permission')
        continue
    print(f"  Total Size: {getDiskSize(partition_usage.total)}")
    print(f"  Used: {getPecentageFormat(partition_usage.percent)} - {getDiskSize(partition_usage.used)}")
    print(f"  Free: {getPecentageFormat(round(100 - partition_usage.percent, 1))} - {getDiskSize(partition_usage.free)}")

diskIo = psutil.disk_io_counters()
print(f"Total read: {getDiskSize(diskIo.read_bytes)}")
print(f"Total write: {getDiskSize(diskIo.write_bytes)}")
