# 구글링을 통해 힌트를 얻어 진행하였으며, 노션 제출 코드는 제가 메모장코딩으로 올린것입니다#
import sys

def print_Star(n):
	if n < 3:
		return ["*"]
	
	num = n // 3

	s = print_Star(num)
	result = []

	for i in s:
		result.append(i * 3)
		result.append(i + " " * num + i)
		result.append(i * 3)


	# for i in s:
		

	# for i in s:
		

	return result

print("\n".join(print_Star(int(sys.stdin.readline()))))
