a = int(input())

## 1부터 합이 X보다 커지는 순간 구하기 
i = 1
cnt = 0

while True:
    cnt += i # 1 -> 3 -> 6 -> 10 -> 15
    if cnt >= a :
        break
    i += 1

sum = i + 1

## sum이 홀수면 분자가 작은 데에서 시작함.
## sum이 짝수면 분모가 작은 데에서 시작함.

front = 0

for i in range(1, sum-1):
    front += i

j = a - front
if sum % 2 == 0:
    # (sum-1, 1), (sum-2, 2), ..., (1, sum-1)
    print(sum - j , '/', j, sep='')
else:
    # 홀수
    print(j, '/', sum-j, sep='')