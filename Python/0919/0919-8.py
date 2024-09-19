import weakref

class Temp:
    def __del__(self):
        print("인스턴스가 삭제되었습니다.")
        
obj1 = Temp()
obj2 = weakref.ref(obj1)

# 약한 참조 시 obj1이 삭제되면 obj2도 삭제됨
obj1 = None

print("end of code")