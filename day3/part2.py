map = {}
input = 347991

def getFromMap(coords):
    try:
        return map[coords]
    except:
        return 0

def calcNew(coords):
    x = coords[0]
    y = coords[1]
    left = (x-1, y) #left
    right = (x+1, y) #right
    up = (x, y+1) #up
    down = (x, y-1) #down

    downright = (x+1, y-1)
    downleft = (x-1, y-1)
    upright = (x+1, y+1)
    upleft = (x-1, y+1)

    sum = getFromMap(left) + getFromMap(right) + getFromMap(down) + getFromMap(up);
    sum = sum + getFromMap(downleft) + getFromMap(downright) + getFromMap(upright) + getFromMap(upleft)
    return sum

def stepCoord(coords, direction):
    x = coords[0]
    y = coords[1]
    if direction == 0: #right
        return (x+1,y)
    elif direction == 1: #up
        return (x,y+1)
    elif direction == 2: #left
        return (x-1,y)
    elif direction == 3: #down
        return (x,y-1)
    else:
        print("FATAL ERROR")
map[(0,0)] = 1;
# map[(0,1)] = calcNew((0,1));

direction = 0 #right
sidelength = 1
coords = (0,0)
goal = 0

while getFromMap(coords) <= input:
    for i in range(0, sidelength):
        coords = stepCoord(coords, direction)
        map[coords] = calcNew(coords);
        if map[coords] > input:
            goal = map[coords]
            print(goal)
            exit()
        pass
    direction = (direction+1)%4
    for i in range(0, sidelength):
        coords = stepCoord(coords, direction)
        map[coords] = calcNew(coords);
        if map[coords] > input:
            goal = map[coords]
            print(goal)
            exit()
        pass
    direction = (direction+1)%4
    sidelength = sidelength + 1;
