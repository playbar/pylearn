#!/usr/bin/env python
import subprocess
import os

def get_disk_uper(path):
    #计算磁盘分区使用率，
    #其中f_blocks是分区的总块数，换算成G
    #f_bavail是分区的可用块数，换算成G
    info = os.statvfs(path)
    total = round(float(info.f_bsize * info.f_blocks)/1024/1024/1024, 2)
    free = round(float(info.f_bsize * info.f_bavail)/1024/1024/1024, 2)
    return 100 - int(float(free) / float(total) * 100)

def get_disk_info():
    disk_info = {}
    (status, output) = subprocess.getstatusoutput('df -h ')
    #status是执行命令的返回值，默认情况下0是成功，非0是失败
    if status != 0:
        print (status, output)
        return
    #分析返回内容，对返回内容以换行符作为分割
    for line in output.split("\n"):
        #只对/dev/ 分区设备获取使用率
        if not line.startswith('/dev/'):
            continue
        #对一行内容按照空格或者tab进行分割，以提取分区字段名称
        temp = line.split()
        if len(temp) < 2:
            continue
        #获取分区名
        dev_name = temp[0]
        dev_used = get_disk_uper(dev_name)
        print ("[%s] = %d%%"%(dev_name, dev_used))

if __name__ == "__main__":
    get_disk_info()

