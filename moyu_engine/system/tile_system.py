
import sys 
sys.path.append('moyu_engine') 

import components as c

class TileSystem:
    def __init__(self):
        self.data = c.data.Data()
        self.assets = c.assets.Assets()
        self.tilemap = c.tilemap.Tilemap()

        self.config = {
                        'data':self.data.config,
                        'assets':self.assets.config,
                        'tilemap':self.tilemap.config,
                        }

    def set(self):
        self.config['data']['xlsx_path'] = 'tinyland\\data\\tile.xlsx'
        self.data.xlsx()
        print(self.data.data)
        self.config['assets']['sheet_dictionary'] = self.data.sheet
        self.config['assets']['data_dictionary'] = self.data.data
        self.config['assets']['path'] = 'tinyland\\assets\\graphics\\tile'
        self.assets.set()
        print(self.config['assets']['data_dictionary'])

if __name__=="__main__":
    tilesystem = TileSystem()
    tilesystem.set()