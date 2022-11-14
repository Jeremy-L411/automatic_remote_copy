import os
import time
import sys
import shutil
from rich.progress import track

src = "/source/to/files"
dst = "destination/folder"


print("connecting to VPN", file=sys.stdout)
os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command connect split_tunnel.ovpn')

time.sleep(8)

print("Ensuring VPN Connection, waiting 90 seconds", file=sys.stdout)
time.sleep(90) # adjust your connection time

# Mounting Drive
os.system(r"net use W: \\server_address\TimeMachine password /user:user /persistent:no")

time.sleep(8)

# copying files
os.system(r"python.exe copy_status.py {0} {1}".format(src, dst))

# unmounting Drive
os.system(r"net use W: /Delete")

os.system(r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --command disconnect split_tunnel.ovpn')
print("Disconnected from VPN", file=sys.stdout)

print("Enjoy your Movies", file=sys.stdout)

time.sleep(10)