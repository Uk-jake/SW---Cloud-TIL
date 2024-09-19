import threading, time

g_count = 0
lock = threading.Lock()

class ThreadEx(threading.Thread):
    def run(self):

        global g_count
        global lock
    
        for i in range(10):
            lock.acquire()
            print('id={0} 증가하기 전 --> {1}'.format(self.getName(), g_count))
            g_count = g_count + 1
            time.sleep(0.5)
            print('id={0} 증가한 후 --> {1}'.format(self.getName(), g_count))
            lock.release()
            time.sleep(0.5)


for i in range(2):
    th = ThreadEx()
    th.start()