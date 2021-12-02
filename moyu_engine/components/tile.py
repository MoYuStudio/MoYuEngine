
import xlrd

class Tile:
    def __init__(self,tile_data={
                                    'id':0,
                                    'name':'tile_name',
                                    'assets':None,
                                    'effect':None,
                                }):
        self.tile_data = tile_data

    def read(self):
        book = xlrd.open_workbook('moyu_engine\data\tile.xlsx')

        sheet = book.sheet_by_name('tileland')

        for i in range(sheet.nrows):
            print(sheet.row_values(i))

if __name__ == "__main__":
    tile = Tile()
    tile.read()
