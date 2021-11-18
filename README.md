# Python101L_Assignment11
 
if __name__ == '__main__':
    hours = int(input('What is the current hour ==> '))

    minutes = int(input('What is the current minute ==> '))

    second = int(input('What is the current second ==> '))

    clock = Clock(hours, minutes, second)

while True:
print(clock)
clock.tick()
time.sleep(1)

if __name__ == '__main__':
    hours = int(input('What is the current hour ==> '))

    minutes = int(input('What is the current minute ==> '))

    seconds = int(input('What is the current second ==> ')



while True:
    print("{02} : {02} : {02}".format(hours, minutes, seconds))
    seconds += 1
    time.sleep(1)