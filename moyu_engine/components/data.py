
import xlrd
import xlwt

class Data:
    def __init__(self,config = {
                                    # xlsx
                                    'xlsx_path':r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\moyu_engine\data\tile.xlsx',
                                    'nrows_or_ncols':'ncols',
                                }):
        self.config = config
        self.data = []

    def xlsx(self):

        xlsx_data = xlrd.open_workbook(self.config['xlsx_path'])
        sheets_name = xlsx_data.sheet_names()

        self.sheet = []

        for sheet_name in sheets_name:
            sheet_data = xlsx_data.sheet_by_name(sheet_name)
            self.sheet.append(sheet_data)

            sheet_nrows = sheet_data.nrows  #行
            sheet_ncols = sheet_data.ncols  #列

            if self.config['nrows_or_ncols'] == 'ncols':

                self.title = []

                for ncols_title_num in range(sheet_ncols):
                    self.title.append(sheet_data.cell_value(rowx=0, colx=ncols_title_num))

                for nrows_num in range(sheet_nrows-1):
                    data_dict ={}
                    for ncols_num in range(sheet_ncols):
                        data_dict[self.title[ncols_num]] = sheet_data.cell_value(rowx=nrows_num+1, colx=ncols_num)

                    self.data.append(data_dict)

        return self.data,self.sheet,self.title

if __name__ == "__main__":
    data = Data()
    data.xlsx()