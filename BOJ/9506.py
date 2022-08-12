while True:
    num = int(input())

    if num == -1:
        break

    numbers=[]

    sum = 0

    for i in range (1,num):
        if num%i == 0:
            sum+=i
            numbers.append(str(i))
                
    if num == sum:
        print(num, '=', " + ".join(numbers))

    else:
        print(num, "is NOT perfect.")