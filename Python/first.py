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

x = 5
print(f"before callByValue() x is {x}")
callByValue(x)
print(f"after callByValue() x is {x}")