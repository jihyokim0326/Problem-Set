# BOJ 2675 : https://www.acmicpc.net/problem/2675

num = int(input()) # number of testcases

# alphanumeric = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:")

for i in range (num):
    a, b= input().split()
    a= int(a)
    b = str(b)

    ans = ''
    for l in list(b):
        for j in range(a):
            print(l, end='')
    print()