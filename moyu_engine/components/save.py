
import pickle

class Save:
    def __init__(self):

        self.path = 'moyu_engine/config/'
        self.slot_name = 'save'
        self.write_data = {}
        self.read_data = {}

    def write(self):
        f=open(self.path + self.slot_name,'wb')
        pickle.dump(self.write_data, f)
        f.close()
    def read(self):
        f=open(self.path + self.slot_name,'rb')
        self.read_data = pickle.load(f)
        f.close()
        
        return self.read_data

if __name__ == "__main__":
    pass