S = input()
lst_s = list(S.lower())
idx_s = sorted(list(set(S.lower())))            #인덱스만들기

cnt_s = {}
for idx in range(len(idx_s)):                   
    count = 0
    for alpha in range(len(lst_s)):
        if idx_s[idx] == lst_s[alpha]:      # 알파벳 숫자세기
            count += 1
    cnt_s[idx_s[idx]] = count               # 인덱스별 몇개인지 저장

cnt = 0
for key, val in cnt_s.items():
    if max(cnt_s.values()) == val:             #최대값은 몇개인가
        cnt += 1
        maxi_str = key
if cnt > 1:                         # 1개이상이면 ?
    print('?')
else:                               #아니면 출력
    print(maxi_str.upper())
