# 클래스 선언
class Student :
    # 리턴할 인스턴스를 저장할 변수
    __instance = False
    
    def __new__(cls, *args, **kwargs):
        # 인스턴스가 만들어지지 않았으면 인스턴스를 생성하고 그렇지 않으면 기존 인스턴스를 리턴
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def __init__(self, name, num):
        self.name = name
        self.num = num
    
student1 = Student("jake", 25)

print(student1.name)

student2 = Student("emma", 30)

print(student2.name)

print( student1 is student2)