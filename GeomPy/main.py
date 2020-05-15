size = 3
cord_arr = []
count = 0

for x in range(0,size):
    for y in range(0,size):
        cord_arr.append([x,y])

for x1,y1 in cord_arr:
    for x2,y2 in cord_arr:
        if x2 - x1 > 0 and y2 - y1 > 0:
            count+=1

def checkCount(size): 
    size -= 1
    return (size * size * (size + 1) * (size + 1)) // 4

print(cord_arr)
print('Count via Coordinate checking: ',count)
print('Count ',checkCount(size))
