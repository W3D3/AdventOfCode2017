input = 347991
# input = 23;

def getDiam(x):
    return x*2-1

def getRightCorner(x):
    if x == 1:
        return 1
    else:
        diam = getDiam(x)
        # print(diam)
        return diam * diam


print("AoC 2017 - Day 3 / Part 1")

if input == 1:
    print(0)
    exit()

detected = False
j = 1
found = 0

while detected == False:
    # print(x)
    if getRightCorner(j) > input:
        # print(getDiam(j))
        x = j-1;
        y = -j+1;
        found = getRightCorner(j);
        # print(getRightCorner(j))
        detected = True



        #go left next
        # for i in range(x, x-getDiam(x), -1):
        #     if found == input:
        #         print("FOUND!!!")
        #         print(i)
        #         print(y)
        #         break
        #     found = found - 1;


    else:
        j = j + 1

diameter = getDiam(j)
stepsleft =  found - input
# print("stepsLeft:"+str(stepsleft))
info = divmod(stepsleft, diameter-1)
# print(info)
# print("x:"+str(x)+",y:"+str(y))
if info[0] == 3:
    x = x;
    y = y + (diameter-1) - info[1]
elif info[0] == 2:
    x = x - (diameter-1) + info[1]
    y = y + (diameter-1)
elif info[0] == 1:
    x = x - (diameter-1)
    y = y + info[1]
elif info[0] == 0:
    x = x - (info[1])
    y = y
# elif info[0] == 4:
#     x

print("x:"+str(x)+",y:"+str(y))

print(abs(x)+abs(y))
