N= int(input())

A= str(input())

sum = 0
cnt = 0

for i in list(A):
    cnt += 1
    if cnt<= N:
        sum+= int(i)

print(sum)

# while True:
#     cnt += 1
#     if cnt > N:
#         break
#     sum += int(list(A)[cnt-1])

# print(sum)