
import time, click
  
# Made 5/31/22
# output is now showing the right time, but is still a little glitchy. Replace click.progressbar with spinner or differnt progress bar system. It works perfectly for times
# under a minute, but gets glitchy for times over one minute.

# The dream is for this to become part of a command line tool. I want it to be as quick and easy as possible to make a simple timer for making tea.
# I want to be able to enter "tea 2" into a command line and get a two minute timer, or "tea 30" to get a 30 second timer. One digit means minutes and 
# two digits means seconds.


def minToSec(t):
    s = str(t)
    if len(s) == 1:
        q = t * 60
        
    if len(s) >= 2:
        q = t

    return(q)

def progbar(z):
    
    try:
        timeSeconds = minToSec(int(z))
    except:
        timeSeconds = 120

    with click.progressbar(range(timeSeconds), show_eta=False) as bar:
        
        
        for i in bar:
            p = timeSeconds - i
            mins, secs = divmod(p, 60)
            timer = '  {:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            i = i + 1     
        print('\nTime Over')


z = input("Time: ")

progbar(z)



   
