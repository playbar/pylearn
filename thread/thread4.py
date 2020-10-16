#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
class MyThread(threading .Thread ):
    def __init__(self,delay,name,count):
        threading .Thread .__init__(self)
        self .delay=delay
        self.name=name
        self.count=count
    def run (self):
        print('starting'+ self.name )
        threadLock.acquire()
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        print_time(self.delay ,self.name ,self.count)
        # 释放锁
        threadLock.release()
def print_time(delay,name,count):
    while count :
        time.sleep(delay )
        print("{}:{}".format(name, time.ctime(time.time())))
        count  -= 1

threadLock=threading.Lock()
#创建容器（列表）
threads=[]
# 创建新线程
thread1=MyThread(1,'thread-1',3)
thread2=MyThread(2,'thread-2',3)
# 开启新线程
thread1.start()
thread2 .start()
# 添加线程到线程容器（列表）
threads .append(thread1 )
threads .append(thread2 )
# 等待所有线程完成
for t in threads :
    t.join()
print('Exiting Main Thrid')

