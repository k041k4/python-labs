#create temporary directory for labs
import os
os.mkdir('temp')

#write to file
fout = open('temp\oops.txt','wt')
print('yeah', file=fout)
fout.write('anything')
fout.close()

#read file
fin = open('introducing-python-labs\chapter-1-2.py','rt')
read_all = fin.read()
fin.close()

#read lines
fin = open('introducing-python-labs\chapter-1-2.py','rt')
lines = fin.readlines()
fin.close()
line_number = 0
for line in lines:
    line_number += 1
    print(line_number, line, end='')

#read/write binary
bdata = bytes(range(0, 256))
fout = open('temp\oops.bin','wb')
fout.write(bdata)
fout.close()

fin = open('temp\oops.bin','rb')
bdata = fin.read()
print(bdata[32:127].decode('ASCII')) # just a visible ASCII Characters to avoid exception
fin.close()

#file system operations
import os
print('file exists:', os.path.exists('temp\oops.bin'))
print('is this abolute path:', os.path.isabs('temp\oops.bin'))
print(os.path.abspath('temp'))
print(os.path.realpath('temp'))

print(os.listdir('temp'))
import shutil
shutil.rmtree('temp')

#pathlib - new advanced library for paths
from pathlib import Path
file_path = Path('temp') / 'oops.txt'
print(file_path)
print(file_path.suffix)