# 1. subprocess的run、call、check_call、check_output函数
# subprocess.run(args[, stdout, stderr, shell ...])：执行args命令，返回值为CompletedProcess类；
# 若未指定stdout，则命令执行后的结果输出到屏幕上，函数返回值CompletedProcess中包含有args和returncode；
# 若指定有stdout，则命令执行后的结果输出到stdout中，函数返回值CompletedProcess中包含有args、returncode和stdout；
# 若执行成功，则returncode为0；若执行失败，则returncode为1；
# 若想获取args命令执行后的输出结果，命令为：output = subprocess.run(args, stdout=subprocess.PIPE).stdout
#
# subprocess.call(args[, stdout, ...])：执行args命令，返回值为命令执行状态码；
# 若未指定stdout，则命令执行后的结果输出到屏幕；
# 若指定stdout，则命令执行后的结果输出到stdout；
# 若执行成功，则函数返回值为0；若执行失败，则函数返回值为1；
# （类似os.system）
#
# subprocess.check_call(args[, stdout, ...])：执行args命令，返回值为命令执行状态码；
# 若未指定stdout，则命令执行后的结果输出到屏幕；
# 若指定stdout，则命令执行后的结果输出到stdout；
# 若执行成功，则函数返回值为0；若执行失败，抛出异常；
# （类似subprocess.run(args, check=True)）
#
# subprocess.check_output(args[, stderr, ...])：执行args命令，返回值为命令执行的输出结果；
# 若执行成功，则函数返回值为命令输出结果；若执行失败，则抛出异常；
# （类似subprocess.run(args, check=True, stdout=subprocess.PIPE).stdout）
#
# （1） args：启动进程的参数，默认为字符串序列（列表或元组），也可为字符串（设为字符串时一般需将shell参数赋值为True）；
# （2） shell：shell为True，表示args命令通过shell执行，则可访问shell的特性；
# （3） check：check为True时，表示执行命令的进程以非0状态码退出时会抛出；subprocess.CalledProcessError异常；check为False时，状态码为非0退出时不会抛出异常；
# （4） stdout、stdin、stderr：分别表示程序标准标输出、输入、错误信息；
# run函数返回值为CompletedProcess类，若需获取执行结果，可通过获取返回值的stdout和stderr来捕获；
# check_output函数若需捕获错误信息，可通过stderr=subprocess.STDOUT来获取；



import subprocess

# subprocess.run使用
def subprocess_run():
    print("**** subprocess.run ****")
    print("----------")
    result1 = subprocess.run(["adb", "devices"])
    print("result1:", result1)
    print("----------")
    result2 = subprocess.run("adb devices", shell=True, check=True)
    print("result2:", result2)
    print("----------")
    result3 = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE)
    print("result3:", result3)
    print(type(result3))
subprocess_run()
"""结果
**** subprocess.run ****
----------
List of devices attached
338b123f0504    device

result1: CompletedProcess(args=['adb', 'devices'], returncode=0)
----------
List of devices attached
338b123f0504    device

result2: CompletedProcess(args='adb devices', returncode=0)
----------
result3: CompletedProcess(args=['adb', 'devices'], returncode=0, stdout=b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n')
<class 'subprocess.CompletedProcess'>
"""

# subprocess.call使用
def subprocess_call():
    print("**** subprocess.call ****")
    print("----------")
    result1 = subprocess.call(["adb", "devices"])
    print("result1:", result1)
    print("----------")
    result2 = subprocess.call(["adb", "devices"], stdout=subprocess.PIPE)
    print("result2:", result2)
subprocess_call()
"""结果
**** subprocess.call ****
----------
List of devices attached
338b123f0504    device

result1: 0
----------
result2: 0
"""

# subprocess.check_call
def subprocess_check_call():
    print("**** subprocess.check_call ****")
    print("----------")
    result1 = subprocess.check_call(["adb", "devices"])
    print("result1:", result1)
    print("----------")
    result2 = subprocess.check_call(["adb", "devices"], stdout=subprocess.PIPE)
    print("result2:", result2)
subprocess_check_call()
"""结果
**** subprocess.check_call ****
----------
List of devices attached
338b123f0504    device

result1: 0
----------
result2: 0
"""

# subprocess.check_output
def subprocess_check_output():
    print("**** subprocess.check_output ****")
    print("----------")
    result1 = subprocess.check_output(["adb", "devices"])
    print("result1:", result1)
    print("----------")
    result2 = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE).stdout
    print("result2:", result2)
subprocess_check_output()

