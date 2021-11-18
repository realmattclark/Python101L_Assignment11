import time


if __name__ == '__main__':
    hours = int(input('What is the current hour ==> '))

    minutes = int(input('What is the current minute ==> '))

    second = int(input('What is the current second ==> '))

    class Clock:
        def __init__(self, hours, minutes, seconds, tick):
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
    
        def hours(self):
            return self.hours
    
        def minutes(self):
            return self.minutes
        
        
        def tick(self):
            seconds = 0
            seconds += 1
            return self.tick

        def show(self):
            print("{02} {02} {02}".format(hours, minutes, tick)

        
    
    clock = Clock(hours, minutes, seconds)


def __str__(self, hours, minutes, tick):
    print('{02} : {02} : {02}'.format(hours, minutes, tick))


while True:
    print(clock)
    Clock.tick()
    time.sleep(1)