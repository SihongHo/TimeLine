import numpy as np
import argparse

# python timeline.py --start-time 8
def parse_args():
    parser = argparse.ArgumentParser("Computing Timeline")
    parser.add_argument("--start-time", type=float, default=8, help="get up time")
    return parser.parse_args()
    
def get_time_line(start_time):
    # get_up_time = 8
    first_pick = 6
    second_pick = 4
    dip = 4
    sleep_time = 7
    warm_up_time = 1.5
    cool_down_time = 1.5
    time_list = [warm_up_time, first_pick, dip, second_pick, cool_down_time]
    time_name = ["First pick", "Dip", "Second pick", "Cool down", "Sleep"]
    # print(sum(time_list) + sleep_time)
    print("-------------------------------------")
    print("Get up at %0.1f h"%(start_time))
    for i in range(len(time_list)):
        start_time = (start_time + time_list[i])%24%12
        print("-------------------------------------")
        print(time_name[i] + " begin at %0.1f h"%(start_time))
        if "pick" in time_name[i] or "Dip" in time_name[i]:
            mid_time = (time_list[i+1]/2 + start_time)%24%12
            end_time = (time_list[i+1] + start_time)%24%12
            print(time_name[i] + "'s midlle begin at %0.1f h"%(mid_time))
            print(time_name[i] + " end at %0.1f h"%(end_time))
    print("-------------------------------------")

if __name__ == '__main__':
    arglist = parse_args()
    get_time_line(arglist.start_time)
