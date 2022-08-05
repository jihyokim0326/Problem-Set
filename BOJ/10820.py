# BOJ : https://www.acmicpc.net/problem/10820
import sys

while True:
    lines = sys.stdin.readline().rstrip('\n')
 
    if not lines:
        break

    upper = 0
    lower = 0
    space=0
    numbers=0

    for w in lines:
        if w.islower():
            lower+=1


    for j in lines:
        if j.isupper():
            upper+=1

    for x in lines:
        if x.isnumeric():
            numbers+=1

    for y in lines:
        if y.isspace():
            space+=1

    print(lower, upper, numbers, space)
