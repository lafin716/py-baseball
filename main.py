import random
from collections import OrderedDict

print("야구 게임시작~")
# 숫자 야구게임은 랜덤한 3개의 숫자를 맞추는 게임입니다.
# 정답의 각 숫자는 1~9 사이의 중복되지 않은 숫자 3개로 구성된다.
# 답은 중복되지 않은 1~9 사이의 3개의 숫자를 입력한다.
# 정답은 3개의 숫자와 위치까지 모두 맞춰야 한다.
# 규칙은 아래와 같다
# 1. 기회는 3번 주어진다
# 2. 숫자도 맞고 위치도 맞으면 스트라이크
# 3. 숫자는 있으나 위치가 안맞으면 볼
# 4. 숫자가 아예 없으면 아웃

# 게임 실행 여부
is_running = True

# 정답 기회
chance = 3

# 정답 생성
collect_nums = []
while len(collect_nums) < 3:
    rand_num = random.randint(1, 9)
    collect_nums.append(rand_num)
    collect_nums[:] = list(OrderedDict.fromkeys(collect_nums))
print(collect_nums)

# 게임 시작
while is_running:
    # 남은기회
    print("남은 기회 : %d" % chance)

    # 사용자입력
    answer = input("숫자를 입력해주세요 : ")
    if len(answer) != 3:
        print("3자리만 입력해라")
        continue
    answer_nums = list(OrderedDict.fromkeys(answer))
    if len(answer_nums) != 3:
        print("중복 안됨 ㅋ")
        continue
    answer_nums = list(answer_nums)

    # 정답 비교
    strike = 0
    ball = 0
    out = 0
    for i in range(len(answer_nums)):
        is_out = True
        for j in range(len(collect_nums)):
            if int(answer_nums[i]) == collect_nums[j]:
                if i == j:
                    strike = strike + 1
                    is_out = False
                    break
                ball = ball + 1
                is_out = False
                break
        if is_out:
            out = out + 1

    print("=========================")
    print("스트라이크 : %d" % strike)
    print("볼 : %d" % ball)
    print("아웃 : %d" % out)
    print("=========================")
    chance = chance - 1

    # 스트라이크가 3이면 종료
    if strike == 3:
        print("축하드립니다 정답입니다!")
        break

    # 기회가 0이면 종료한다
    if chance <= 0:
        print("기회를 모두 사용하였습니다")
        break

print("게임을 종료합니다")