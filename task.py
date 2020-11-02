#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.

import random

def current_orientation():
    return random.randrange(0,360)

def new_orientation(current_orientation, rate_of_correction):
    return current_orientation+random.gauss(0, 2*rate_of_correction)

def tilt_correction(current_orientation, rate_of_correction):
    return ((current_orientation+random.randrange(0,360))/4)%360

if __name__=="__main__":
    orientation=current_orientation()
    rate_of_correction=random.random()

    while(True):
        print("write 'stop'- to end the loop, anything else to continue")
        x = input()
        if(x=="stop"):
            break

        current=new_orientation(orientation, rate_of_correction)
        print("current orientation: {}".format(current))

        correction=tilt_correction(current, rate_of_correction)

        print("with correction {corr}: {final}".format(final=(current+correction)%360, corr=correction))