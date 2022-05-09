import sys

a= list(map(int, sys.stdin.readline().split()))

val = a[3]-a[1]
val2 = a[1]
val3 = a[2]-a[0]
val4 = a[0]

print(min(val, val2, val3, val4))