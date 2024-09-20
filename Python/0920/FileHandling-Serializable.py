import pickle

class VO:
    def __init__(self, num = 0, name = ""):
        self.num = num
        self.name = name
    
    # Setter
    def setNum(self, num):
        self.num = num
    def setName(self, name):
        self.name = name
    
    # Getter
    def getNum(self):
        return self.num
    def getName(self):
        return self.name
    
    # 인스턴스 출력하기 위해서 인스턴스를 참조하는 데이터를 출력하는 데이터를 반환
    def __str__(self):
        return f"num: {self.num}, name: {self.name}"

data1 = VO(1, "Ava")
data2 = VO(2, "Bob")
li = [data1, data2]
# 객체를 파일에 직접 저장 - Serializable
# with open('./Python/0920/serial.txt', 'wb') as f:
#     pickle.dump(li, f)

with open('./Python/0920/serial.txt', 'rb') as f:
    result = pickle.load(f)
    for voData in result:
        print(voData)
    