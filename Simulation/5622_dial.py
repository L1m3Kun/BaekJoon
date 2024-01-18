# 5622 다이얼
def find_num(alphabet_list):
    num = 0
    for alphabet in alphabet_list:      #아스키코드를 이용한 변환
        if 64 < ord(alphabet) < 68:
            num +=  2
        elif ord(alphabet) < 71:
            num +=  3
        elif ord(alphabet) < 74:
            num +=  4
        elif ord(alphabet) < 77:
            num +=  5
        elif ord(alphabet) < 80:
            num +=  6
        elif ord(alphabet) < 84:
            num +=  7
        elif ord(alphabet) < 87:
            num +=  8
        elif ord(alphabet) < 91:
            num +=  9
        else:
            num += 10
    return num + len(alphabet_list)     # 숫자 합 + 문자 길이
    

S = input()
print(find_num(S))
