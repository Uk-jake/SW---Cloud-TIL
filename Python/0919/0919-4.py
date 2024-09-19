try:
    x = int(input('3의 배수를 입력하세요: '))
    # 조건이 맞지 않으면 AssertionError 발생
    assert x % 3 == 0, "3의 배수 아닙니다." # x가 3의 배수가 아니면
    print(x)
except AssertionError as e: # 예외가 발생했을 때 실행됨 
    print('예외가 발생했습니다.', e)