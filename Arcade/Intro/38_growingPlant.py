'''
Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight, your task is to find how many days it'll take for the plant to reach this height.

Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
'''

def growingPlant(upSpeed, downSpeed, desiredHeight):
    days=0
    height=0
    while(True):
        days+=1
        height+=upSpeed
        if(height>=desiredHeight):
            return days
        height-=downSpeed
