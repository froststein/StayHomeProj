def makeFace(side):
    arr = []
    for i in range(0,3):
        arr.append([side,side,side])
    return arr

arr_O = makeFace('O')
arr_G = makeFace('G')
arr_W = makeFace('W')
arr_B = makeFace('B')
arr_R = makeFace('R')
arr_Y = makeFace('Y')

arr_Test = ['F','R','U','B','L','D','F','Rp','U','Bp','L','Dp','Fp','R','Up','B','Lp','D']

def printCube():
    for row in arr_W:
        print(' - - - ',' '.join(row),' - - - - - - ')
    for i in range(0,3):
        print('', ' '.join(arr_O[i]),'',' '.join(arr_G[i]),'',' '.join(arr_R[i]),'',' '.join(arr_Y[i]),'')
    for row in arr_B:
        print(' - - - ',' '.join(row),' - - - - - - ')

def sideRotations(in_arr, side_Index, val_arr):
    for i in range(0,3):
        in_arr[i][side_Index] = val_arr[i]

def topbottomRotations(in_arr, top_bottom_Index, val_arr):
    for i in range(0,3):
        in_arr[top_bottom_Index][i] = val_arr[i]

printCube()
while(True):
#for choice in arr_Test:
    choice = input('Choose move: F, Fp, L, Lp, U, Up, D, Dp, R, Rp, B, Bp \n')
    if(choice == 'F'):
        # green array rotate
        arr_G=  [list(cubeside) for cubeside in zip(*reversed(arr_G))]
        # store tmp values
        tmp_arr_R = [row[0] for row in arr_R]
        tmp_arr_O = [row[2] for row in arr_O]
        #change red layer
        sideRotations(arr_R,0,arr_W[2])
        #change orange layer
        sideRotations(arr_O,2,arr_B[0])
        #change white layer
        topbottomRotations(arr_W,2,tmp_arr_O[::-1])
        #change blue layer
        topbottomRotations(arr_B,0,tmp_arr_R[::-1])

    if(choice == 'Fp'):
        for i in range(0,3):
            # green array rotate
            arr_G=  [list(cubeside) for cubeside in zip(*reversed(arr_G))]
            # store tmp values
            tmp_arr_R = [row[0] for row in arr_R]
            tmp_arr_O = [row[2] for row in arr_O]
            #change red layer
            sideRotations(arr_R,0,arr_W[2])
            #change orange layer
            sideRotations(arr_O,2,arr_B[0])
            #change white layer
            topbottomRotations(arr_W,2,tmp_arr_O[::-1])
            #change blue layer
            topbottomRotations(arr_B,0,tmp_arr_R[::-1])

    if(choice == 'L'):
        #Orange Rotation
        arr_O=  [list(cubeside) for cubeside in zip(*reversed(arr_O))]
        #G>B>Y>W
        tmp_arr_B = [row[0] for row in arr_B]
        tmp_arr_G = [row[0] for row in arr_G]
        tmp_arr_W = [row[0] for row in arr_W]
        tmp_arr_Y = [row[2] for row in arr_Y]
        sideRotations(arr_G,0,tmp_arr_W)
        sideRotations(arr_W,0,tmp_arr_Y[::-1])
        sideRotations(arr_Y,2,tmp_arr_B[::-1])
        sideRotations(arr_B,0,tmp_arr_G)

    if(choice == 'Lp'):
        for i in range(0,3):
            #Orange Rotation
            arr_O=  [list(cubeside) for cubeside in zip(*reversed(arr_O))]
            #G>B>Y>W
            tmp_arr_B = [row[0] for row in arr_B]
            tmp_arr_G = [row[0] for row in arr_G]
            tmp_arr_W = [row[0] for row in arr_W]
            tmp_arr_Y = [row[2] for row in arr_Y]
            sideRotations(arr_G,0,tmp_arr_W)
            sideRotations(arr_W,0,tmp_arr_Y[::-1])
            sideRotations(arr_Y,2,tmp_arr_B[::-1])
            sideRotations(arr_B,0,tmp_arr_G)

    if(choice == 'U'):
        #White rotation
        arr_W=  [list(cubeside) for cubeside in zip(*reversed(arr_W))]
        #G>O>Y>R, Left shift by 3
        tmp_arr_O = arr_O [0]
        tmp_arr_G = arr_G [0]
        tmp_arr_R = arr_R [0]
        tmp_arr_Y = arr_Y [0]
        arr_O[0] = tmp_arr_G
        arr_G[0] = tmp_arr_R
        arr_R[0] = tmp_arr_Y
        arr_Y[0] = tmp_arr_O

    if(choice == 'Up'):
        for i in range(0,3):
            #White rotation
            arr_W=  [list(cubeside) for cubeside in zip(*reversed(arr_W))]
            #G>O>Y>R, Left shift by 3
            tmp_arr_O = arr_O [0]
            tmp_arr_G = arr_G [0]
            tmp_arr_R = arr_R [0]
            tmp_arr_Y = arr_Y [0]
            arr_O[0] = tmp_arr_G
            arr_G[0] = tmp_arr_R
            arr_R[0] = tmp_arr_Y
            arr_Y[0] = tmp_arr_O

    if(choice == 'D'):
        #Blue Rotation
        arr_B=  [list(cubeside) for cubeside in zip(*reversed(arr_B))]
        #O>G>R>Y 
        tmp_arr_O = arr_O [2]
        tmp_arr_G = arr_G [2]
        tmp_arr_R = arr_R [2]
        tmp_arr_Y = arr_Y [2]
        arr_O[2] = tmp_arr_Y
        arr_G[2] = tmp_arr_O
        arr_R[2] = tmp_arr_G
        arr_Y[2] = tmp_arr_R

    if(choice == 'Dp'):
        for i in range(0,3):
            #Blue Rotation
            arr_B=  [list(cubeside) for cubeside in zip(*reversed(arr_B))]
            #O>G>R>Y 
            tmp_arr_O = arr_O [2]
            tmp_arr_G = arr_G [2]
            tmp_arr_R = arr_R [2]
            tmp_arr_Y = arr_Y [2]
            arr_O[2] = tmp_arr_Y
            arr_G[2] = tmp_arr_O
            arr_R[2] = tmp_arr_G
            arr_Y[2] = tmp_arr_R

    if(choice == 'R'):
        #Red Rotation
        arr_R=  [list(cubeside) for cubeside in zip(*reversed(arr_R))]
        #G>W>Y>B
        tmp_arr_B = [row[2] for row in arr_B]
        tmp_arr_G = [row[2] for row in arr_G]
        tmp_arr_W = [row[2] for row in arr_W]
        tmp_arr_Y = [row[0] for row in arr_Y]
        sideRotations(arr_G,2,tmp_arr_B)
        sideRotations(arr_W,2,tmp_arr_G)
        sideRotations(arr_Y,0,tmp_arr_W[::-1])
        sideRotations(arr_B,2,tmp_arr_Y[::-1])

    if(choice == 'Rp'):
        for i in range(0,3):
            #Red Rotation
            arr_R=  [list(cubeside) for cubeside in zip(*reversed(arr_R))]
            #G>W>Y>B
            tmp_arr_B = [row[2] for row in arr_B]
            tmp_arr_G = [row[2] for row in arr_G]
            tmp_arr_W = [row[2] for row in arr_W]
            tmp_arr_Y = [row[0] for row in arr_Y]
            sideRotations(arr_G,2,tmp_arr_B)
            sideRotations(arr_W,2,tmp_arr_G)
            sideRotations(arr_Y,0,tmp_arr_W[::-1])
            sideRotations(arr_B,2,tmp_arr_Y[::-1])

    if(choice == 'B'):
        #Yellow Rotation
        arr_Y=  [list(cubeside) for cubeside in zip(*reversed(arr_Y))]       
        #O>W>R>B
        tmp_arr_O = [row[0] for row in arr_O]
        tmp_arr_W = arr_W[0]
        tmp_arr_R = [row[2] for row in arr_R]
        tmp_arr_B = arr_B[2]

        sideRotations(arr_O,0,tmp_arr_W[::-1])
        topbottomRotations(arr_W,0,tmp_arr_R)
        sideRotations(arr_R,2,tmp_arr_B[::-1])
        topbottomRotations(arr_B,2,tmp_arr_O)

    if(choice == 'Bp'):
        for i in range(0,3):
            #Yellow Rotation
            arr_Y=  [list(cubeside) for cubeside in zip(*reversed(arr_Y))]       
            #O>W>R>B
            tmp_arr_O = [row[0] for row in arr_O]
            tmp_arr_W = arr_W[0]
            tmp_arr_R = [row[2] for row in arr_R]
            tmp_arr_B = arr_B[2]

            sideRotations(arr_O,0,tmp_arr_W[::-1])
            topbottomRotations(arr_W,0,tmp_arr_R)
            sideRotations(arr_R,2,tmp_arr_B[::-1])
            topbottomRotations(arr_B,2,tmp_arr_O)
            
    printCube()

