# 10950.py : https://www.acmicpc.net/problem/10950
import sys
t= int(input())

for i in range (t):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)