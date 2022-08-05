# BOJ : https://www.acmicpc.net/problem/1157

word = input()

letters = list(word)
ascii = []

for l in letters:
    n = ord(l)

    if n >= 97:
        n -= 32
    ascii.append(n)

ascii_dict = {}

# {'1' : 3} key, value

for a in ascii:
    if a in ascii_dict.keys():
        ascii_dict[a] += 1
    else:
        ascii_dict[a] = 1    

max_num = max(list(ascii_dict.values()))

cnt = 0
ans = None
for k, v in ascii_dict.items():
    if v == max_num:
        cnt += 1
        ans = k

if cnt > 1:
    print('?')
else:
    print(chr(ans))