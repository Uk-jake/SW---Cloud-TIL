import abc

# 추상 클래스 - 인스턴스를 생성할 수 없습니다.
class Restaurant(metaclass=abc.ABCMeta):
    # 추상 메서드 - 내용이 없는 메서드
    @abc.abstractmethod
    def food(self):
        pass
    
# 추상 클래스를 상속받는 클래스
# 추상 클래스를 상속받는 클래스는 추상 메서드를 반드시 구현해야 합니다.
class Sub(Restaurant):
    def food(self):
        print("음식을 만듭니다.")

sub = Sub()
sub.food()