import os
from pathlib import Path

if __name__ == '__main__':
    # Test and show usage
    import sys


    print('CURRENT DIR')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)


    print ('Before:')
    for x in sys.path: print(x)

    print('ALL SUBFOLDERS')

 #   subfolders = [ f.path for f in os.scandir(dir_path) if f.is_dir() ]


#    for f in Path(dir_path).iterdir():
#       print(f)

    path = Path.cwd()
    for e in [i for i in path.iterdir() if i.is_dir()]:
        print(e)



 #   print(subfolders)
