# BOJ 4153 : https://www.acmicpc.net/problem/4153

a = list(map(int, input().split()))

while True:
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break

    maximum=max(a)

    a.remove(maximum)
    if a[0]*a[0]+ a[1]*a[1]==maximum*maximum:
        print("right")

    else:
        print('wrong')
    
    a = list(map(int, input().split()))