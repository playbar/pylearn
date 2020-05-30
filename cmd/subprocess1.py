# subprocess.getoutput(cmd)：执行cmd命令，返回值为命令执行的输出结果（字符串类型）；
# 注：执行失败，不会抛出异常（类似os.popen(cmd).read()）；
#
# subprocess.getstatusoutput(cmd)：执行cmd命令，返回值为元组类型(命令执行状态, 命令执行的输出结果)；
# 元组中命令执行状态为0，表示执行成功；命令执行状态为1，表示执行失败；

import subprocess;
# subprocess.getoutput或getstatusoutput使用
def subprocess_get_output():
    print("**** subprocess.getoutput ****")
    result1 = subprocess.getoutput("adb devices")
    print("result1:", result1)
    print(type(result1))

    print("**** subprocess.getstatusoutput ****")
    result2 = subprocess.getstatusoutput("adb devices")
    print("result2:", result2)
    print(type(result2))
subprocess_get_output()

