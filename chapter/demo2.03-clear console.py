import os
import sys
#打开out.log文件
f_handler=open('out.log','w')
#保存默认的python标准输出
oldstdout=sys.stdout
#将python标准输出指向out.log
sys.stdout=f_handler
#清空python控制台
os.system('cls')
#恢复python默认的标准输出
sys.stdout=oldstdout