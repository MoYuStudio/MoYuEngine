
import pickle

import config.data.constants as C

class SavaSystem:
    
    def save_tilemap():

        f=open('moyu_engine/config/data/game_save','wb')
        save_data = {'window':C.window}
        pickle.dump(save_data, f)
        f.close()

    def read_tilemap():

        f=open('moyu_engine/config/data/game_save', 'rb')
        read_data = pickle.load(f)
        C.window = read_data['window']
        f.close()