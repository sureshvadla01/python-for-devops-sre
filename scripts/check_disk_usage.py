import shutil

total, used, free = shutil.disk_usage("/")
percent_used = (used / total) * 100
print(f"Disk usage on / : {percent_used:.2f}%")
