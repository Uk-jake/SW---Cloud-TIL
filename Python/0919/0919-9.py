import time, threading

def worker(name, delay):
    for i in range(3):
        time.sleep(delay)
        print(f"{name} is working...")
        
# 일반 함수 실행
#worker("Bob", 1)
#worker("Alice", 1)

# 스레드 생성
thread1 = threading.Thread(target = worker, args = ("Alice", 0.5))
thread2 = threading.Thread(target = worker, args = ("James", 0.5))

# 스레드 실행
thread1.start()
thread2.start()