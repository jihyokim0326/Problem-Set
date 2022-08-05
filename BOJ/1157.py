# BOJ : https://www.acmicpc.net/problem/1157

word = input().upper()

letters = list(word)

letter_dict = {}
for a in letters:
    if a in letter_dict.keys():
        letter_dict[a] += 1
    else:
        letter_dict[a] = 1    

max_num = max(list(letter_dict.values()))

cnt = 0
ans = None
for k, v in letter_dict.items():
    if v == max_num:
        cnt += 1
        ans = k

if cnt > 1:
    print('?')
else:
    print(ans)
