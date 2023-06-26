import os
def read_dir_as_list(path,with_root = True,with_suffix = True,sort_rm_suffix = False):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    if sort_rm_suffix:
        files.sort(key = lambda x : int(x[:-4]))
    else:
        files.sort()
    s=[]
    
    for line in files:
        strl = os.path.join(path,line) if with_root else line 
        strl = strl if with_suffix else os.path.splitext(strl)
        s.append(strl)
    return s