rooms = []

for i in range(15):
    l = []
    for j in range(14):
       l.append(None) 
    rooms.append(l)

rooms[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for s in range(1, 15):
    for i in range(14):
        temp = 0
        for j in range(i+1):
            temp += rooms[s-1][j]
        rooms[s][i] = temp

T = int(input())

for i in range(T):
    a = int(input())
    b = int(input())

    print(rooms[a][b-1])