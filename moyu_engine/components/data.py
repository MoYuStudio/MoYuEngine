
import xlrd
import xlwt

class Data:
    def __init__(self,data = {}):
        self.data = data

    def xlsx(self,xlsx_path = r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\moyu_engine\data\tile.xlsx',nrows_or_ncols = 'ncols'):

        xlsx_data = xlrd.open_workbook(xlsx_path)
        sheets_name = xlsx_data.sheet_names()

        for sheet_name in sheets_name:
            sheet_data = xlsx_data.sheet_by_name(sheet_name)

            sheet_nrows = sheet_data.nrows  #行
            sheet_ncols = sheet_data.ncols  #列

            if nrows_or_ncols == 'ncols':

                ncols_title = []
                self.data = []

                for ncols_title_num in range(sheet_ncols):
                    ncols_title.append(sheet_data.cell_value(rowx=0, colx=ncols_title_num))

                for nrows_num in range(sheet_nrows-1):
                    data_dict ={}
                    for ncols_num in range(sheet_ncols):
                        data_dict[ncols_title[ncols_num]] = sheet_data.cell_value(rowx=nrows_num+1, colx=ncols_num)

                    self.data.append(data_dict)

            print(self.data)

        return self.data






        # sheets_data = xlsx_data.sheets()


        # xlsx_data = xlrd.open_workbook(xlsx_path)
        # sheets = xlsx_data.sheets()
        # print(sheets)
        # sheet = xlsx_data.sheet_by_name('land')

        # cell_info = sheet.cell(rowx=1, colx=1)
        # print(cell_info)

        # nrows = sheet.nrows  #获取该sheet中的有效行数
        # print(nrows)

        # ncols = sheet.ncols#获取列表的有效列数
        # print(ncols)

if __name__ == "__main__":
    data = Data()
    data.xlsx()