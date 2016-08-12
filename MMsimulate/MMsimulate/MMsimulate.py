import pandas as pd
import os

import os
import time

def print_ts(message):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)

def run(interval):
    #Excute for the first time
    print_ts("-"*100)
    print_ts("Starting every %s seconds."%interval)
    print_ts("-"*100)

    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval-time.time()%interval
            print_ts("Sleeping until %s (%s seconds)..."%((time.ctime(time.time()+time_remaining)), time_remaining))
            time.sleep(time_remaining)
            print_ts("Starting command.")

            # execute the command
            print("this is a test for endless loop")
            print_ts("-"*100)
            
        except Exception as e:
            print(e)


def MM():
    pass

def initial():
    #input the frequency table and form
    df=pd.read_csv("warship.csv")
    print(df)


if __name__=="__main__":
    interval = 5
    command = r"ipconfig"
    run(interval, command)
