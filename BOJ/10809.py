alphabets = []
index = []

letters = list(input()) # baekjoon -> ['b', 'a', 'e', 'k']
 
for num in range(97, 123):
    alphabets.append(chr(num))

for i in alphabets:
    if i in letters:
        idx = str(letters.index(i))
    else:
        idx = str(-1)
    index.append(idx)

result = " ".join(index)
print(result)
