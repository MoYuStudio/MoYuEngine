
import os
import xlrd
import xlwt

class Data:
    def __init__(self):
        self.config =  {
                            # xlsx
                            'xlsx_path':'moyu_engine/data/config.xlsx',
                            'nrows_or_ncols':'nrows',
                        }
        self.data = {}

        self.os_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    def xlsx(self):

        xlsx_data = xlrd.open_workbook(self.os_path +'/'+ self.config['xlsx_path'])
        sheets_name = xlsx_data.sheet_names()
        self.sheet = sheets_name

        for sheet_num in range(len(sheets_name)):
            self.data[sheets_name[sheet_num]] = []
            sheet_data = xlsx_data.sheet_by_name(sheets_name[sheet_num])

            sheet_nrows = sheet_data.nrows  # 行
            sheet_ncols = sheet_data.ncols  # 列

            # 获取每一列的数据
            if self.config['nrows_or_ncols'] == 'nrows':

                self.title = []

                for nrows_title_num in range(sheet_nrows):
                    self.title.append(sheet_data.cell_value(rowx=nrows_title_num, colx=0))

                for ncols_num in range(sheet_ncols-1):
                    data_dict ={}
                    for nrows_num in range(sheet_nrows):
                        data_dict[self.title[nrows_num]] = sheet_data.cell_value(rowx=nrows_num, colx=ncols_num+1)

                    self.data[sheets_name[sheet_num]].append(data_dict)

            # 获取每一行的数据
            if self.config['nrows_or_ncols'] == 'ncols':

                self.title = []

                for ncols_title_num in range(sheet_ncols):
                    self.title.append(sheet_data.cell_value(rowx=0, colx=ncols_title_num))

                for nrows_num in range(sheet_nrows-1):
                    data_dict ={}
                    for ncols_num in range(sheet_ncols):
                        data_dict[self.title[ncols_num]] = sheet_data.cell_value(rowx=nrows_num+1, colx=ncols_num)

                    self.data[sheets_name[sheet_num]].append(data_dict)

        return self.data,self.sheet,self.title

if __name__ == '__main__':
    data = Data()
    data_dict,sheet,title = data.xlsx()
    print(data_dict)
    #print(sheet)
    #print(title)
