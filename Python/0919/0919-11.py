import threading, time

shareData = []

# 스레드 동기화를 위한 Condition 객체 생성
cv = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        global shareData
        global cv
        
        for i in range(10):
            cv.acquire()
            print(f"공유 자원 생성 : {i}")
            shareData.append(i)
            time.sleep(0.1)
            cv.notify()
            cv.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global shareData
        global cv
        
        for i in range(10):
            cv.acquire()
            if len(shareData) < 1:
                print("공유 자원 소비 대기")
                cv.wait(2)
                print("공유 자원 소비 대기 종료")
                
            
            print(f"공유 자원 소비 : {shareData.pop()}")
            cv.release()
            time.sleep(1)

producer = Producer()
consumer = Consumer()

consumer.start()
producer.start()
