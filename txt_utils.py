
def readlines(filename):
    """Read all the lines in a text file and return as a list
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines
    
def writelines(filename,list_w):
    '''Write a list to a TXT file '''
    with open(filename,'w') as f:
        for line in list_w:
            f.write(line)
            f.write('\n') 