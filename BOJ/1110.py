N= int(input())

def find_next(N):
    num = N%10
    num2= (N%100- N%10)/10
    sum= num + num2
    product= 10*(N%10)
    return product + sum


print(find_next(26))
# if product+sum = N:
#     print("%d"\i)
