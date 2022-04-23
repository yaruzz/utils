import os
def read_dir_as_list(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    files.sort(key = lambda x : int(x[:-4]))
    s=[]
    
    for line in files:
        strl = os.path.join(path,line)
        s.append(strl)
    return s