
import pickle

class Save:
    def __init__(self):
        pass
    def save(self):
        f=open('moyu_engine/config/data/game_save','wb')
        save_data = {'map':[]}
        pickle.dump(save_data, f)
        f.close()
    def read(self):
        f=open('moyu_engine/config/data/game_save', 'rb')
        data = pickle.load(f)
        tilemap = data['map']
        f.close()