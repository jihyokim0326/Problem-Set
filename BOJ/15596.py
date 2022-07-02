# function solve(a : list) -> intL
#  .....
# return __ (int)


import sys
def solve(a : list) -> int:
    
    sum = 0
    for i in a:
        sum+=i
    return sum

if __name__ == '__main__':
    numbers = list(map(int, sys.stdin.readline().split()))
    result = solve(numbers)
    print(result)