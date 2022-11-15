import os
import time
import sys


print("connecting to VPN, waiting 90 seconds for secure connection", file=sys.stdout)

#connecting to VPN
os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command connect split_tunnel.ovpn')
time.sleep(8)


for i in range(90):
    print(i, file=sys.stdout)
    time.sleep(1)


# Mounting Drive
os.system(r"net use W: \\NAS\Path password /user:user /persistent:no")

time.sleep(8)
# copying files
os.system(r"python.exe C:\scripts\copy_status.py W:\location\of\media C:\location\to\save")

# unmounting Drive
os.system(r"net use W: /Delete")

os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command disconnect split_tunnel.ovpn')
print("Disconnected from VPN", file=sys.stdout)

time.sleep(10)
