#60print("Hello World")

import time

seconds = int(input("Type Number of Second"))

# 

def timer(userInput):

    while userInput>0:
        minutes=int(userInput/60)
        seconds=int(userInput % 60)

        displayTime=f"{minutes}:{seconds}"

        print(displayTime)
        time.sleep(1)
        userInput=userInput-1

    print("Time's Up")

timer(seconds)


# number=10

# while number>0:
#     print(number)
#     number=number-1