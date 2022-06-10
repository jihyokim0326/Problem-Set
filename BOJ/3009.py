# BOJ 3009 : https://www.acmicpc.net/problem/3009

a,b= map(int, input().split())
c,d=map(int, input().split())
e,f=map(int, input().split())

if a==c:
    g=e
elif a==e:
    g=c
else:
    g=a

if b==d:
    h=f
elif b==f:
    h=d
else:
    h=b

print(g,h)