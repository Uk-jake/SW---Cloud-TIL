# super()를 이용한 부모 클래스의 메소드 호출
class super():
    # 생성자
    def __init__(self):
        print("super 생성자")
        self.score = 0

    def greeting(self):
        print("Hello, I'm super")

# sub 클래스는 super 클래스를 상속받음        
class sub(super):
    def __init__(self):
        # 상위 클래스의 초기화 메서드를 호출해야지만 상위 클래스 속성을 사용할 수 있음.
        super.__init__(self)
        self.name = "tmp"
    
    # 상위 클래스 Method overriding
    def greeting(self):
        # overring는 재사용이 아닌 확장이기 때문에 상위 클래스의 메소드를 호출하려면 super()를 사용해야 함
        super.greeting(self)
        print("Hello, I'm sub")
    
    def sayGoodbye(self):
        print("Goodbye")
        
    def superGreeting(self):
        super.greeting(self)
        
subInst = sub()

subInst.greeting()
#subInst.sayGoodbye()

# sub가 super의 서브인지 확인
#print(issubclass(sub, super))

#print(subInst.name)
#print(subInst.score)
