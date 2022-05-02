# 10818.py : https://www.acmicpc.net/problem/10818
import sys
N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

max = -1000000
min = 1000000

for num in numbers:
    if num> max:
        max = num
    if num < min:
        min = num

print(min,max)
