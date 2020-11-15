from abc import ABC, abstractmethod
from random import gauss
import logging
from math import log

class Event(ABC):
    @abstractmethod
    def result_of_event(self, yaw, roll, pitch):
        pass

class Turbulence(Event):
    def __init__ (self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def result_of_event(self, yaw, roll, pitch):
        yaw=yaw+gauss(self.mu, self.sigma)
        roll=roll+gauss(self.mu, self.sigma)
        pitch=pitch+gauss(self.mu, self.sigma)
        return (yaw, roll, pitch)
    
class Correction(Event):
    def __init__(self, rate_of_correction):
        self.rate_of_correction=rate_of_correction

    def result_of_event(self, yaw, roll, pitch):
        mu=0
        sigma_param=2
        yaw=yaw-gauss(mu, sigma_param*self.rate_of_correction)
        roll=roll-gauss(mu, sigma_param*self.rate_of_correction)
        pitch=pitch-gauss(mu, sigma_param*self.rate_of_correction)
        return (yaw, roll, pitch)

class Environment:
    def __init__(self, mass):
        self.mass=mass
        self.turbulence = Turbulence(0, 5)

    def create_turbulence(self, x, y, yaw, roll, pitch):
        temp = (x + y)/(x * y) + log(self.mass)
        (y,r,p)=self.turbulence.result_of_event(yaw, roll, pitch)
        return (temp*y, temp*r, temp*p)

class Plane:
    def __init__(self, x, y, mass, rate_of_correction):
        self.x = x
        self.y = y
        self.yaw = 0
        self.roll = 0
        self.pitch = 0
        self.environment = Environment(mass)
        self.correction = Correction(rate_of_correction)
        logging.basicConfig(format='%(message)s', level=logging.INFO)
    
    def current_orientation(self):
        while True:
            self.x += 10
            self.y += 10
            (y,r,p) = self.environment.create_turbulence(self.x, self.y, self.yaw, self.roll, self.pitch)
            self.yaw = (self.yaw+y)%360
            self.roll = (self.yaw+r)%360
            self.pitch = (self.yaw+p)%360
            logging.info("current orientation:\n\tyaw: {}, roll: {}, pitch: {}".format(self.yaw, self.roll, self.pitch))
            yield (self.yaw, self.roll, self.pitch)
    
    def correct_orientation(self):
        while True:
            (self.yaw, self.roll, self.pitch) = self.correction.result_of_event(self.yaw, self.roll, self.pitch)
            logging.info("corrected orientation:\n\tyaw: {}, roll: {}, pitch: {}".format(self.yaw, self.roll, self.pitch))
            yield (self.yaw, self.roll, self.pitch)
        
if __name__ == "__main__":
    plane = Plane(0, 0, 10000, 0.2)
    while True:
        try:
            next(plane.current_orientation())
            next(plane.correct_orientation())
        except KeyboardInterrupt:
            print("End of simulation")
            break