N= int(input())

def find_next(N):
    num = N%10
    num2= (N%100- N%10)/10
    sum= (num + num2) % 10
    product= 10*(N%10)
    return int(product + sum)

cnt = 0
next = N

while True:
    next = find_next(next)
    cnt += 1

    if next == N:
        break
print(cnt)