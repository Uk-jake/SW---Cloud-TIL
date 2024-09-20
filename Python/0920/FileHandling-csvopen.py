try:
    # with 블럭을 사용하면 with안에서 파일을 열고 작업을 마치면 자동으로 파일을 닫아준다.
    # 한글이 포함된 경우 encoding='utf8'을 추가해야 한다.
    with open("./Python/0920/data.csv", 'r', encoding='utf8') as file:
        #content = file.readline()
        #print(content)
        
        for line in file.readlines():
            print(line.split(','))
        
except Exception as e:
    print(f"파일 쓰기 중 예외 발생 : {e}")
