import os   
print("===========================>os.system")
os.system('dir')



# import os   
tmp = os.popen('ls *.sh').readlines()
print("===========================>os.popen")
print(tmp)




# Subprocess是一个功能强大的子进程管理模块，是替换os.system ,os.spawn* 等方法的一个模块。
# import subprocess   
# subprocess.call (["cmd", "arg1", "arg2"],shell=True)  
# 好处在于:运用对线程的控制和监控，将返回的结果赋于一变量，便于程序的处理。

import subprocess
p = subprocess.Popen('ls *.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)   

print("===========================>subprocess.Popen")
print(p.stdout.readlines())

for line in p.stdout.readlines():
    print (line)

retval = p.wait()