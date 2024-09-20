try:
    
    #with open("./Python/0920/test.bin", "wb") as file:
        # 문자열을 byte로 변환해서 기록
        #file.write('안녕하세요'.encode())
        
        
    with open("./Python/0920/test.bin", "rb") as file:
        byteArray = file.read()
        print(byteArray)
        print(byteArray.decode())
        
except Exception as e:
    print(f"파일 쓰기 중 예외 발생 : {e}")
