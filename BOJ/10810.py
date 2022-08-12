# BOJ : https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())

baskets = [0] * N

for m in range(M):
    i, j, k = map(int, input().split())

    for n in range(i, j+1):
        baskets[n-1] = k

baskets = list(map(str, baskets))

print(' '.join(baskets))
