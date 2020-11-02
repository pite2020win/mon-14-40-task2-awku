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