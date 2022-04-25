import sys

N, X = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for i in numbers:
    if i< X:
        print(i,end=' ')