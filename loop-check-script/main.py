import os
import time
from datetime import datetime
from webscrape.HOP_scrap import HOP_scrap

wing = input("What is your wing number? ")
floor = input("What is your floor number? 0, 1 or 2? ")
side = input("Which side do you live in? Left or Right? ")
TIME_SPAN_MINS = int(input("For how long do you want to run the check? (in mins) "))
HOP_list = HOP_scrap(wing, floor, side)

INTERVAL_SPAN_SECS = 3.5

output_file = open("ping_results.txt", "a")  # Open file in append mode

while True:
    total_pings = 0
    num_fails = 0
    max_uptime = 0
    max_downtime = 0
    curr_uptime = 0
    curr_downtime = 0
    num_downtime = 0

    for i in range(int(TIME_SPAN_MINS * 60 / INTERVAL_SPAN_SECS)):
        for j in HOP_list:
            IP = HOP_list[j]
            response = os.system("ping -c 1 " + IP + " >/dev/null 2>&1")
            total_pings += 1
            if response == 0:
                output = f"\033[92m{datetime.now()}: {IP} Active"
                max_downtime = max(curr_downtime, max_downtime)
                curr_downtime = 0
                curr_uptime += 1
            else:
                num_fails += 1
                max_uptime = max(max_uptime, curr_uptime)
                if curr_uptime != 0:
                    num_downtime += 1
                    curr_uptime = 0
                    curr_downtime += 1
                    output = f"\033[91m{datetime.now()}: {IP} Ping Failed"
            
            
            print(output)
            
            
            output_file.write(output + "\n")

        time.sleep(INTERVAL_SPAN_SECS)
    out_fail = f"Num pings: {total_pings}\nPings Failed: {num_fails}\nMax Uptime: {max_uptime}\nNum Downtime: {num_downtime}"
    out_summary = f"Total Time: {total_pings * INTERVAL_SPAN_SECS / 60} mins\nDowntime: {num_fails * INTERVAL_SPAN_SECS / 60} mins\nMax Uptime: {max_uptime * INTERVAL_SPAN_SECS / 60} mins\nMax Downtime: {max_downtime * INTERVAL_SPAN_SECS / 60} mins"
    print(out_fail)
    print(out_summary)
    output_file.write(out_fail+"\n")
    output_file.write(out_summary+"\n")
    output_file.close()  

    