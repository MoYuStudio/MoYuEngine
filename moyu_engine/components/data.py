
import xlrd
import xlwt

class Data:
    def __init__(self,data_data = {
                                    # xlsx
                                    'xlsx_path':r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\moyu_engine\data\tile.xlsx',
                                    'nrows_or_ncols' : 'ncols',
                                },data = {}):
        self.data_data = data_data
        self.data = data

    def xlsx(self):

        xlsx_data = xlrd.open_workbook(self.data_data['xlsx_path'])
        sheets_name = xlsx_data.sheet_names()

        for sheet_name in sheets_name:
            sheet_data = xlsx_data.sheet_by_name(sheet_name)

            sheet_nrows = sheet_data.nrows  #行
            sheet_ncols = sheet_data.ncols  #列

            if self.data_data['nrows_or_ncols'] == 'ncols':

                ncols_title = []
                self.data = []

                for ncols_title_num in range(sheet_ncols):
                    ncols_title.append(sheet_data.cell_value(rowx=0, colx=ncols_title_num))

                for nrows_num in range(sheet_nrows-1):
                    data_dict ={}
                    for ncols_num in range(sheet_ncols):
                        data_dict[ncols_title[ncols_num]] = sheet_data.cell_value(rowx=nrows_num+1, colx=ncols_num)

                    self.data.append(data_dict)

        return self.data

if __name__ == "__main__":
    data = Data()
    data.xlsx()