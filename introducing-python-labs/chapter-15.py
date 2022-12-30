# Execute OS commands and get output
import subprocess
import os

ret = subprocess.getstatusoutput('dir') #execute as subrpocess
print(ret)
os.system('dir') #execute directly

# system info
import psutil
import platform
print(platform.uname())
print('\n', psutil.cpu_times(True))

#