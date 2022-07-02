import sys

a, b = map(int, sys.stdin.readline().split())

gcd = 0
for i in range(b, 0 , -1):
    if b%i==0 and a%i==0:
        gcd = i
        break


lcm = int(a*b/gcd)

print(gcd)
print(lcm)