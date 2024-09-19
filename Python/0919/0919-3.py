try:
    # 예외가 발생할 수 있는 코드
    x = int(input("숫자를 입력하세요: "))
    result = 10 / x
# as 뒤에 변수명을 적으면 에러 메시지를 변수에 저장할 수 있다.
except ZeroDivisionError as e:
    # 0으로 나눌 때 발생하는 에러 처리
    print("0으로 나눌 수 없습니다.")
    print(f"Error name : {e}")
    result = None
except ValueError as e:
    # 입력이 숫자가 아닐 때 발생하는 에러 처리
    print("잘못된 입력입니다. 숫자를 입력하세요.")
    print(f"Error name : {e}")
else :
    # 예외가 발생하지 않았을 때 실행
    print("예외가 발생하지 않았습니다.")
    print(f" 10 / {x} = {result}")
finally:
    # 예외가 발생하든 안 하든 무조건 실행
    print("프로그램 종료.")