import threading, time
# 세마포어 객체 생성
sema = threading.Semaphore(3) 

lock = threading.Lock()

class ThreadEx(threading.Thread):
    def run(self): 
        sema.acquire()
        #lock.acquire() 
        time.sleep(1) 
        print(self.getName()) 
        #lock.release()
        sema.release()
        
for i in range(10): 
    th = ThreadEx() 
    th.start()