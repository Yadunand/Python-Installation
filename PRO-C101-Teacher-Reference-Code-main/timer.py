from ast import While
from threading import Timer
import time 

def countDown_Timer (seconds): 
    while seconds >0:
        mins=int(seconds/60)
        secs=int(seconds%60)

        timer = f'{mins}:{secs}'
        print(timer)
        seconds-=1 

    print("timeup")

seconds=input("Enter the time in number of seconds :")

countDown_Timer(int(seconds))


 
