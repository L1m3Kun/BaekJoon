"""
penter,pexit,pescape,data는 0과 1로 구성된 문자열
2<= len(penter) <= 100
penter, pexit, pescape 는 상이
2 <= len(data) <= 100,000, len(penter) 의 배수
"""


def solution(penter: str, pexit: str, pescape: str, data: str) -> str:
    answer = ""
    N = len(penter)
    data_len = len(data)
    for i in range(0, data_len, N):
        if data[i : i + N] in (penter, pexit, pescape):
            answer += pescape + data[i : i + N]
        else:
            answer += data[i : i + N]
    return penter + answer + pexit


if __name__ == "__main__":
    # penter = input().strip()
    # pexit = input().strip()
    # pescape = input().strip()
    # data = input().strip()
    # testcase 1
    # 110011011001100110010010111100111001110000000010
    # 110011011001100110010010111100111001110000000010
    print(solution("1100", "0010", "1001", "1101100100101111001111000000"))
    # testcase 2
    # 100000010010001111
    # 100000010010001111
    print(solution("10", "11", "00", "00011011"))
