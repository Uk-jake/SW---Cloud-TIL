# 파일 읽기 시 예외 처리
try:
    with open("./Python/0923/words.txt", 'r') as file:
        # 파일의 각 줄 출력
        for line in file:
            # 줄바꿈 문자 제거
            tmp = line.strip()
            # 문자열 뒤집기
            reversed_tmp = tmp[::-1]
            # 회문이라면 출력
            if tmp == reversed_tmp:
                print(tmp)

except Exception as e:
    print(f"파일 읽기 중 예외 발생 : {e}")