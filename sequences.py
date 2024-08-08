# Python file with definitions of 3:00, 5:00, and 10:00 sequences

import time

def countdownOutput(currentTime):
    print(currentTime)


'''Function to run the 3:00 sequence
3:00 - 3 Long beeps
2:00 - 2 Long beeps
1:30 - 1 Long beep and 3 short beeps
1:00 - 1 Long beep
0:30 - 3 short beeps
0:20 - 2 short beeps
0:10 - 1 short beep
0:05 - 1 short beep
0:04 - 1 short beep
0:03 - 1 short beep
0:02 - 1 short beep
0:01 - 1 short beep
0:00 - 1 Long beep
GO!'''
def threeMin():
    start = time.time()
    if time.time() - start >= 180:
        countdownOutput("3:00")
    elif time.time() - start >= 120:
        countdownOutput("2:00")
    elif time.time() - start >= 90:
        countdownOutput("1:30")
    elif time.time() - start >= 60:
        countdownOutput("1:00")
    elif time.time() - start >= 30:
        countdownOutput("0:30")
    elif time.time() - start >= 20:
        countdownOutput("0:20")
    elif time.time() - start >= 10:
        countdownOutput("0:10")
    elif time.time() - start >= 5:
        countdownOutput("0:05")
    elif time.time() - start >= 4:
        countdownOutput("0:04")
    elif time.time() - start >= 3:
        countdownOutput("0:03")
    elif time.time() - start >= 2:
        countdownOutput("0:02")
    elif time.time() - start >= 1:
        countdownOutput("0:01")
    else:
        countdownOutput("0:00")
    return

def fiveMin():
    return

def tenMin():
    return

threeMin()