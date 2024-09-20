data = []
dict = {}
sum = 0

try:
    with open("./Python/0920/log.txt", "r") as logFile:
        content = logFile.readlines()
        
        for line in content:
            data.append(line.strip().split(" "))
        
        print(f"data length: {len(data)}")
        
        for line in data:
            # 숫자를 제외한 모든 문자열 제거
            if line[9] == "-" or line[9] == "\"-\"":
                line[9] = 0
            else:
                line[9] = int(line[9])
            
            # dict 키 존재 여부 확인
            if line[0] in dict:
                dict[line[0]] = dict[line[0]] + line[9]
            else:
                dict[line[0]] = line[9]    
        
            sum = sum + int(line[9])
        
        print(len(dict))
        
        for data in dict:
            print(f"{data} : {dict[data]}")
        
        print(sum)
            
except FileNotFoundError:
    print("File not found")
    