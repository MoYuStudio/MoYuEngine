
import pickle

import data.constants as C

class SavaSystem:
    
    def save_tilemap():

        f=open('moyu_engine/config/data/game_save','wb')
        save_data = {'map':C.tilemap}
        pickle.dump(save_data, f)
        f.close()

    def read_tilemap():

        f=open('moyu_engine/config/data/game_save', 'rb')
        data = pickle.load(f)
        C.tilemap = data['map']
        f.close()