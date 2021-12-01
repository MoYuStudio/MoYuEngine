
import pickle

class Save:
    def __init__(self,path='moyu_engine/data/',slot_name='save',write_data={}):
        self.path = path
        self.slot_name = slot_name
        self.write_data = write_data
        self.read_data = {}
    def write(self):
        f=open(self.path+self.slot_name,'wb')
        pickle.dump(self.write_data, f)
        f.close()
    def read(self):
        f=open(self.path+self.slot_name,'rb')
        self.read_data = pickle.load(f)
        f.close()
        
        return self.read_data

if __name__ == "__main__":
    pass
