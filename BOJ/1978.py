a = int(input())

sum = 0

i = 0

N = []

str_list = input().split() # '1 3 5 7'

for num in str_list:
    num = int(num)
    N.append(num)

for num in N:
    is_prime = True
    
    if num == 1:
        continue

    for i in range(2,num):
        if num%i == 0:
            is_prime= False
    
    if is_prime:
        sum += 1    

print(sum)
