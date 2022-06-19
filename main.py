
# 야구 게임 만들기
import random

def make_set(numbers):
    result = set()
    for i in range(len(numbers)):
        number = numbers[i]
        result.add(number)

    return result

def get_rand_arr(count):
    result = set()
    while len(result) < count:
        result.add(random.randint(1, 9))
    return list(result)

def search(index, number, answers):
    for i in range(len(answers)):
        answer = answers[i]
        if int(number) == answer:
            if index == i:
                return '○'
            return '△'
    return 'X'

is_running = True
number_count = 3
answers = get_rand_arr(number_count)
print(answers)

while is_running:
    number = input("숫자를 입력하세요 : ")
    number = make_set(number)
    if len(number) != number_count:
        print(number_count + "자리만 입력할 수 있습니다.")
        continue

    for i in range(len(number)):
        result = search(i, number[i], answers)
        flag = result != '○'
        is_running = is_running and flag
        print(result, end=' ')
    print()
