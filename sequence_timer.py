#!/usr/bin/python
#To run the timer
import time

#For arguments
import sys

#For sequence creation
import numpy as np

#To create popup
from Tkinter import Tk, mainloop

def multitimer(time_steps):
    while True:
        for time_step in time_steps:
            print "Started at " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            print "Running for %f minutes" %(time_step)
            time.sleep(int(60.0*time_step))
            #when time is over, create dialog box:
            root = Tk() 
            root.title("%d minutes are up!" % (time_step))
            root.lift()
            root.call('wm', 'attributes', '.', '-topmost', '1')
            mainloop()

if __name__ == "__main__":
    if len(sys.argv) not in [5, 6]:
        print("Not the right number of arguments!")
        exit()
    initial_time = float(sys.argv[1])
    final_time = float(sys.argv[2])
    number_different_times_in_series = float(sys.argv[3])

    if sys.argv[4] == 'g':
        initial_time = np.log10(initial_time)
        final_time = np.log10(final_time)
        time_steps = np.logspace(
            initial_time, final_time,
            num=number_different_times_in_series)
    elif sys.argv[4] == 'a':
        time_steps = np.linspace(
            initial_time, final_time,
            num=number_different_times_in_series)
    else:
        print("Please provide g or a as your fourth argument")
        print("g=geometric, a=arithmetic")
        exit()

    multitimer(time_steps)
