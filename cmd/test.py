
# -*- coding: UTF-8 -*-
 
import os

 
print ('test os.system...')
command = 'free -m 1> test.txt'
status = os.system(command)
if status != 0:
    raise Exception('执行系统命令失败, command=%s, status=%s' % (command, status))
    
print ('test os.popen...')
output = os.popen('cat /root/kangkai/test.txt')
print (output.read())
 
# print ('test commands...')
# import commands
# (status, output) = commands.getstatusoutput('ls /root/kangkai/')
# print (status, output)



