
def tot_coroutine():
    tot = 0
    
    while True:
        x = (yield tot)
        tot += x
        #print("tot: ", tot)
        

# 코루틴 인스턴스 생성 - 함수를 실행하는것이 아니고 코루틴 인스턴스 생성
# 함수 내부에 yield를 가지고 있으면 코루틴 함수임
co = tot_coroutine()
print(next(co)) # 처음 yield까지 코드 수행

print(co.send(1))

print("now, coroutine is paused")

print(co.send(2))

co.close()

print("coroutine is closed")