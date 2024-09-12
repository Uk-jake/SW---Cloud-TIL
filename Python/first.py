# 매개변수가 없는 함수
def noArguments() -> None:
    for _ in range(3):
        print("noArguments() called")

# 파이썬에서도 매개변수에 자료형을 기재하주는 것을 권장.
def argFunc(arg1: str) -> None:
    print("argFunc() called with arguments", arg1)

def callByValue(arg1: int) -> None:
    print(f"callByValue() called with arguments {arg1}")
    arg1 = 20
    print(f"arg1 is now {arg1}")

def orderParameter(a:int, b:int) -> None:
    print(f"a is {a}, b is {b}")
    
def tupleReturn() -> tuple:
    return 100, 200
    
# 매개변수가 여러 개인 경우 1개로 대입해서 분할한 후 사용
def personalInfo(name:str, age:int, gender:bool) -> None :
    print(f"name : {name}")
    print(f"age : {age}")
    print(f"gender : {gender}")

personalInfo("Jake", 25, 1)
personalInfo(*["Jack", 23, 1])
personalInfo(*{"name":"Adam", "age": 34, "gender" : 1})
personalInfo(**{"name":"Adam", "age": 34, "gender" : 1})

#orderParameter(b=10, a=20)
#print(tupleReturn())

# 매개변수의 설명을 추가할 수 있음.
def annotationFunction(score : 'int >= 0') -> None :
    print(f"점수 : {score}")

annotationFunction.__doc__ = "설명란 추가"
    
help(annotationFunction)