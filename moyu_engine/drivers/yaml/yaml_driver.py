
import sys
sys.dont_write_bytecode = True

import os

import yaml

class YamlDriver:
    '''
        [ MoYuEngine # Yaml数据管理器 ]
        
    功能:  Yml & Yaml 数据读写

    变量:
        None
        
    调用:
        self.read(self,read_file='data.yml',read_data={}) # 读取单个文件数据
        self.read_all(self,read_path='yml',read_data={}) # 读取文件夹数据库
        self.write(self,write_file='data.yml',write_data={}) # 写入单个文件数据
        self.write_all(self,write_path='yml',write_data={}) # 写入文件夹数据库
    '''
    
    def __init__(self):
        self.write_path = {}
        
    def read(self,read_file='data.yml',read_data={}):
        '''
            读取 yml & yaml 数据 并存入字典 返回
        '''
        with open(read_file) as f: # with 打开文件
            read_data = yaml.load(f, Loader=yaml.FullLoader) # 加载 yaml 数据
                    
        return read_data
    
    def read_global(self,read_file='data.yml',read_data={}):
        '''
            读取 yml & yaml 数据 并存入字典 返回
        '''
        with open(read_file) as f: # with 打开文件
            docs = yaml.load_all(f, Loader=yaml.FullLoader) # 加载 yaml 数据
            for doc in docs: # 遍历 yaml 数据
                for key, value in doc.items(): # 遍历 yaml 数据中的 key & value
                    read_data[key] = value # 将 key & value 存入字典
                    
        return read_data
    
    def read_all(self,read_path='yml',read_data={}):
        '''
            遍历路径 读取 yml & yaml 数据 并存入字典 返回
        '''
        path_folder = os.path.split(read_path)[-1] # 获取指定文件夹名
        for parent,dirnames,filenames in os.walk(read_path): # 遍历路径 parent:父目录 dirnames:子目录 filenames:文件
            for file_name in filenames: # 遍历文件列表
                folder_name = os.path.basename(parent) # 获取文件夹名
                var_name = (os.path.splitext(file_name))[0] # 拆解文件名 去除后缀
                
                with open(parent+'/'+file_name,'r') as f: # with 打开文件
                    if folder_name == path_folder: # 如果 当前文件夹名 == 指定文件夹名
                        self.write_path[var_name] = parent # 将 变量：文件路径 存入写入字典
                        try:
                            read_data[var_name] = self.read(read_file=os.path.join(parent,file_name),read_data={}) # 读取文件并存入字典
                        except:
                            pass
                    else: # 如果 当前文件夹名 != 指定文件夹名
                        self.write_path[folder_name+'_'+var_name] = parent # 将 文件夹名+_+变量：文件路径 存入写入字典
                        try:
                            read_data[folder_name+'_'+var_name] = self.read(read_file=os.path.join(parent,file_name),read_data={}) # 读取文件并存入字典
                        except:
                            pass
                        
        return read_data

    def write(self,write_file='data.yml',write_data={}):
        '''
            写入 yml & yaml 数据
        '''
        with open(write_file, 'w') as f:
            data = yaml.dump(write_data, f)
            
    def write_all(self,write_path='yml',write_data={}):
        '''
            遍历路径 写入 yml & yaml 数据
        '''
        for key,value in write_data.items():
            if key in self.write_path:
                self.write(write_file=os.path.join(self.write_path[key],key+'.yml'),write_data=value)
            else:
                self.write(write_file=os.path.join(write_path,key+'.yml'),write_data=value)

if __name__ == '__main__':
    yd = YamlDriver()
    print(yd.read_all())
    