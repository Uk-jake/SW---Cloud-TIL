# 클래스 선언
class Student :
    # 생성자 및 속성
    def __init__(self, name = "test", age = 20) :
        print(f"{name} 생성자 호출")
        self.name = name
        self.age = age
    
    # 소멸자
    def __del__(self) :
        print(f"{self.name}소멸자 호출")
    
    # getter
    def getName(self) :
        return self.name
    def getAge(self) :
        return self.age
    
    # setter
    def setName(self, name) :
        self.name = name
    def setAge(self, age) :
        self.age = age
    
    # 메소드
    def study(self) :
        print(f"{self.name}은 공부 중")
    
    @staticmethod
    def staticMethod() :
        print("static method 호출")
        
    @classmethod
    def classMethod(cls) :
        print("class method 호출")
        
# 인스턴스 생성
student1 = Student("jake", 25)
student2 = Student()
student3 = Student()

# bound 호출 - 인스턴스가 메서드 호출
student1.study()
student2.study()
student3.study()

Student.staticMethod()
Student.classMethod()