
from collections import OrderedDict
import random


print("ㅇㅑ구 게임시작~")

# 게임 실행 여부
is_running = True

# 정답 생성
collect_nums = []
while len(collect_nums) < 3:
    rand_num = random.randint(1, 9)
    collect_nums.append(rand_num)
    collect_nums[:] = list(OrderedDict.fromkeys(collect_nums))
print(collect_nums)

# 게임 시작
while is_running:
    # 사용자입력
    answer = input("숫자를 입력해주세요 :")
    if len(answer) != 3:
        print("3자리만 입력해라")
        continue
    answer_nums = list(OrderedDict.fromkeys(answer))
    if len(answer_nums) != 3:
        print("중복 안됨 ㅋ")
        continue
    answer_nums = list(answer_nums)

    # 정답 비교
    for i in range(len(collect_nums)):
        for j in range(len(answer_nums)):
            if collect_nums[i] == int(answer_nums[j]):
                if i == j:
                    print('O', end='')
                    continue
                print('B', end='')
                continue
            print('X', end='')
            continue
        print()

    is_running = False