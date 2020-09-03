import os

def py2_to_py3(path):
    Filelist = []
    DirList = []
    for home, dirs, files in os.walk(path):
        for filename in files:#get file name
            [name, extension] = os.path.splitext(filename)#split file name for judge suffix
            if extension=='.py':
                output=os.popen('2to3 -w '+home.replace('\\','/')+'/'+filename)#cmd input is different from string
                pass

    print(Filelist)
    return Filelist

py2_to_py3(r'E:\Profile\download\testbench-master')