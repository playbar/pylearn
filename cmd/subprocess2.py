## subprocess.Popen类
# 1. 介绍
# subprocess.Popen类用于在一个新进程中执行一个子程序，上述subprocess函数均是基于subprocess.Popen类；
#
# 2.操作
# subprocess.Popen(args[, bufsize, stdin, stdout, stderr, ...])：Popen类的构造函数，返回结果为subprocess.Popen对象；
# args：需要执行的系统命令，可为字符串序列（列表或元组，shell为默认值False即可，建议为序列），也可为字符串（使用字符串时，需将shell赋值为True）；
# shell：默认为False，若args为序列时，shell=False；若args为字符串时，shell=True，表示通过shell执行命令；
# stdout、stdin、stderr：分别表示子程序标准输出、标准输入、标准错误，可为subprocess.PIPE、一个有效的文件描述符、文件对象或None。
# 若为subprocess.PIPE：代表打开通向标准流的管道，创建一个新的管道；
# 若为None：表示没有任何重定向，子进程会继承父进程；
# stderr也可为subprocess.STDOUT：表示将子程序的标准错误输出重定向到了标准输出
# bufsize：指定缓冲策略，0表示不缓冲，1表示行缓冲，其它整数表示缓冲区大小，负数表示使用系统默认值0；
# cwd：默认值为None；若非None，则表示将会在执行这个子进程之前改变当前工作目录；
# env：用于指定子进程的环境变量。若env为None，那么子进程的环境变量将从父进程中继承；若env非None，则表示子程序的环境变量由env值来设置，它的值必须是一个映射对象。
# universal_newlines： 不同系统的换行符不同。若True，则该文件对象的stdin，stdout和stderr将会以文本流方式打开；否则以二进制流方式打开。
# （1）subprocess.Popen对象常用方法（如PopenObject为subprocess.Popen对象）
#
# PopenObject.poll() ：用于检查命令是否已经执行结束，若结束返回状态码；若未结束返回None；
# PopenObject.wait([timeout, endtime])：等待子进程结束，并返回状态码；若超过timeout(s)进程仍未结束，则抛出异常；
# PopenObject.send_signal(signal)：发送信号signal给子进程；
# PopenObject.terminate()：停止子进程；
# PopenObject.kill()：杀死子进程；
# PopenObject.communicate([input, timeout])：与进程进行交互（如发送数据到stdin、读取stdout和stderr数据），它会阻塞父进程，直到子进程完成；
# input：表示将发送到子进程的字符串数据，默认为None；
# timeout：超时判断，若超过timeout秒后仍未结束则抛出TimeoutExpired异常；
# communicate返回值：一个元组(stdout_data, stderr_data)
# （2）subprocess.Popen对象的文本或字节流控制
#
# PopenObject.stdin：
# 若PopenObject中stdin为PIPE，则返回一个可写流对象；若encoding或errors参数被指定或universal_newlines参数为True，则此流是一个文件流，否则为字节流。
# 若PopenObject中stdin不是PIPE，则属性为None。
# stdin输入流非None，可执行写操作即PopenObject.stdin.write(s)
#
# PopenObject.stdout：
# 若PopenObject中stdout为PIPE，则返回一个可读流对象；若encoding或errors参数被指定或universal_newlines参数为True，则此流是一个文件流，否则为字节流。
# 若PopenObject中stdout不是PIPE，则属性为None。
# stdout输出流非None，可执行读操作即PopenObject.stdout.read()或.readlines()
#
# PopenObject.stderr：
# 若PopenObject中stderr为PIPE，则返回一个可读流对象；若encoding或errors参数被指定或universal_newlines参数为True，则此流是一个文件流，否则为字节流。
# 若PopenObject中stderr不是PIPE，则属性为None。
# stderr错误流非None，可执行读操作即PopenObject.stderr.read()或.readlines()

import subprocess;

def subprocess_Popen1():
    print("***通过communicate函数分别输出PopenObject对象的输出流和错误流***")
    args = [["adb", "devices"], ["adb", "devices11"]]
    for arg in args:
        popen_object = subprocess.Popen(arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        object_stdout, object_stderr = popen_object.communicate()
        output = {"popen_object": popen_object,
                  "object_stdout": object_stdout,
                  "object_stderr": object_stderr}
        print(output)
    """
    {'popen_object': <subprocess.Popen object at 0x0000000002212400>, 'object_stdout': b'List of devices attached \r\n106D111805005938\tdevice\r\n\r\n', 'object_stderr': b''}
    {'popen_object': <subprocess.Popen object at 0x0000000002577C18>, 'object_stdout': b'', 'object_stderr': b'Android Debug Bridge version 1.0.31\r\n\r\n -a .....}
    """

    print("***通过stdout和stderr方法输出PopenObject对象输出流和错误流***")
    p0 = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    object_stdout = p0.stdout.read()
    p0.stdout.close()
    object_stderr = p0.stderr.read()
    p0.stderr.close()
    print(object_stdout)        # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(object_stderr)        # 结果：b''

    print("***Popen对象stdin写入功能：使用stdout和stderr输出")
    args = ["python", "python3"]
    for arg in args:
        p4 = subprocess.Popen([arg], shell=True, stdout=subprocess.PIPE,
                              stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        p4.stdin.write("print('hello')")
        p4.stdin.close()
        out = p4.stdout.read()
        p4.stdout.close()
        err = p4.stderr.read()
        p4.stderr.close()
        print("out：%s err：%s" % (out, err))
    """
    ***Popen对象stdin写入功能
    out：hello
    err：
    out： err：'python1' 不是内部或外部命令，也不是可运行的程序或批处理文件。
    """

    print("***Popen对象stdin写入功能：使用communicate输出")
    p4 = subprocess.Popen(["python"], stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p4.stdin.write("print('hello')")
    output = p4.communicate()
    print(output)       # 结果：('hello\n', '')

    print("***不含encoding参数***")
    p1 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out1 = p1.stdout.readlines()
    print(out1)         # 结果: [b'List of devices attached \r\n', b'106D111805005938\tdevice\r\n', b'\r\n']

    print("***含encoding参数***")
    p2 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out2 = p2.stdout.readlines()
    print(out2)         # 结果: ['List of devices attached \n', '106D111805005938\tdevice\n', '\n']

    print("***Popen对象检查命令是否结束，等待进程结束")
    print(p2.poll())    # 结果: None
    print(p2.wait())    # 结果: 0
    print(p2.poll())    # 结果: 0

    print("***Popen对象communicate函数，它会阻塞父进程直至子进程完成")
    p3 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out = p3.communicate()[0]
    print(out)          # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(p3.poll())    # 结果：0
subprocess_Popen1()



def subprocess_Popen2():
    """
    1. 通过管道功能，实现adb shell ps | findstr top功能
    2. 直接为args赋值为一个字符串，实现adb shell ps | findstr top功能
    :return:
    """
    print("***通过管道方式***")
    p1 = subprocess.Popen(["adb", "shell", "ps"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["findstr", "top"], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
    print("***通过传一个字符串方式***")
    p3 = subprocess.Popen("adb shell ps | findstr top", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p3.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
subprocess_Popen2()

