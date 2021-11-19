import time


if __name__ == '__main__':

    hours = int(input('What is the current hour ==> '))

    minutes = int(input('What is the current minute ==> '))

    tick = int(input('What is the current second ==> '))


class Clock:


    def __init__(self, hours, minutes, tick):
        self.hours = 0
        self.minutes = 0
        self.tick = 0
    
    def get_hours(self):
        return self.hours
    
    def get_minutes(self):
        return self.minutes
        
        
    def get_tick(self):
        seconds = 0
        seconds += 1
        return self.tick

    def __str__(hours, minutes, tick):
        print('{02} : {02} : {02}'.format(hours, minutes, tick))

        
    
clock = Clock(hours, minutes, tick)


while True:
    print(Clock)
    Clock.tick()
    time.sleep(1)