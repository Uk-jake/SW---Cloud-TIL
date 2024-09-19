# 클래스 선언
class Student :
    # 생성자 및 속성
    # 클래스로부터 만들어진 인스턴스는 name과 num 속성만을 가짐
    __slots__ = ["__name", "__num"]
    def __init__(self, name = "test", num = 0) :
        #print(f"{name} 생성자 호출")
        # 앞에 __를 붙이면 private으로 선언되어 외부에서 접근 불가
        self.__name = name
        self.__num = 0
    
    # getter
    def getName(self):
        print("getter 호출")
        return self.__name
    def getNum(self):
        print("getter 호출")
        return self.__num
    
    # setter
    def setName(self, name):
        print("setter 호출")
        self.__name = name
    def setNum(self, num):
        print("setter 호출")
        self.__num = num

    # property    
    #name = property(fget = getName, fset = setName)
    #num = property(fget = getNum, fset = setNum)
    
    def __add__(self, other):
        return self.__num + other.__num
    
    def __str__(self):
        return f"{self.__name} : {self.__num}"
    
student1 = Student()
student1.setNum(25)
student1.setName("jake")

print(student1)