try:
    # with 블럭을 사용하면 with안에서 파일을 열고 작업을 마치면 자동으로 파일을 닫아준다.
    with open("./Python/0920/test.txt", 'r') as file:
        for line in file:
            print(line, end="")
except Exception as e:
    print(f"파일 쓰기 중 예외 발생 : {e}")
