# BOJ : https://www.acmicpc.net/problem/1316


Number = int(input())
result= Number

for i in range(0, Number):
    word=input()
    for k in range (0, len(word)-1):
        if word[k]==word[k+1]:
            pass
        elif word[k] in word[k+1:]:
            result-=1

            break
print(result)