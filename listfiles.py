# -*- coding: cp936 -*-  
import os  
  
def listdir(path, list_name):  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
#        elif os.path.splitext(file_path)[1]=='.jpeg':  
        else:
            list_name.append(file_path)  

def main():
    list_name=[]
    listdir(r'E:\工作文档',list_name)
    print '\n\n'.join(list_name)

if __name__=='__main__':
    main()
