from webscrape.dhcp_ip_scrap import get_dhcp_ip_pool
from webscrape.HOP_scrap import HOP_scrap
import os


wing  = input("Please enter the wing number: ")
floor = input("Please enter the floor: ")
side = input("Input the side, like Left or Right: ")

list = HOP_scrap(wing, floor, side)


for switch, IP in list.items():
    response = os.system("ping -c 1 " + IP + ">/dev/null 2>&1")

    if response == 0:
        print(f"\033[92m{switch} ({IP}) Active")
    else:
        print(f"\033[91m{switch} ({IP}) Ping Failed")


