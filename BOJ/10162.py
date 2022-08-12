T = int(input())

cnt=0
count=0
last=0


short = 10
medium = 60
long = 300


while True:

    if T >=long:
        cnt+=1
        T = T - long

    elif T >= medium and T < long:
        count+=1
        T = T - medium

    elif T>= short and T < medium:
        last+=1
        T = T - short

    else: # T < 10
        if T == 0:
            print(cnt, count, last)
            break
        else:
            print(-1)
            break
