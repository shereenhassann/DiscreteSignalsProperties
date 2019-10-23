from matplotlib import pyplot as plt
import numpy as np
#plt.plot([5,7,6,4],[7,5,4,3])
#plt.show()

x = 0
y = 0
value = 0
x_points = []
y_points = []
x_after = []
y_after = []


def reverse_point(x, y):
    x = -x
    print("(",x,",",y,")")
    x_after.append(x)
    y_after.append(y)

def shift_point(x, y, value):
    x = x + value
    print("(",x,",",y,")")
    x_after.append(x)
    y_after.append(y)

#msh shaghala if it gives decimal points akbar mn 0.whatever bt3mel round down
def scale_point(x, y, value):
    if x == 0:
        print("( 0 ,",y,")")
    x = int(x/value)
    if x != 0:
        print("(",x,",",y,")")
    x_after.append(x)
    y_after.append(y)



pointsNumber = int( input ("How many points?\n"))


for i in range(0, pointsNumber):
    x = int ( input("x: "))
    x_points.append(x)
    y = int ( input("y: "))
    y_points.append(y)

choice = int(input("Choose property: \n1.Time reverse.\n2.Time shift.\n3.Time scale.\n"))

if(choice == 1):
    for i in range(0, pointsNumber):
        reverse_point(x_points[i], y_points[i])
        
        
        
if(choice == 2):
    shiftValue = int (input("Input shift value:\n"))
    for i in range(0, pointsNumber):
        shift_point(x_points[i], y_points[i], shiftValue)

if(choice == 3):
    scaleValue = float (input("Input scale value:\n"))
    for i in range(0, pointsNumber):
        scale_point(x_points[i], y_points[i], scaleValue)


for i in range(0, pointsNumber):
    plt.bar(x_after[i], y_after[i])
plt.xlabel('time')
plt.show()















