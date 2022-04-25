import sys

A, B = map(int, sys.stdin.readline().split())

if B>=45:
    print(A,B-45)

elif A>=1 and 0<B<45:
    print(A-1,B+15)

else:
    print(23,B+15)
