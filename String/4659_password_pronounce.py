import sys
input = sys.stdin.readline

def isPronounced(word):
    moem_cnt = jaem_cnt = total_moem = 0
    for idx in range(len(word)):
        if word[idx] in moem:
            moem_cnt += 1
            jaem_cnt = 0
            total_moem += 1
        else:
            moem_cnt = 0
            jaem_cnt += 1
        if moem_cnt >= 3 or jaem_cnt >= 3:
            # print(1)
            return 0
        if (moem_cnt == 2 or jaem_cnt == 2) and word[idx] == word[idx-1] and word[idx] not in ['e', 'o']:
            # print(3)
            return 0
    if not total_moem:
        # print(2)
        return 0
    return 1


moem = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input().strip()
    if password == 'end':
        break
    if isPronounced(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
