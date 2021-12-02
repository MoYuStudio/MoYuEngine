
import xlrd
import xlwt

class Data:
    def __init__(self):
        pass

    def xlsx(self):
        xlsx = xlrd.open_workbook(r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\moyu_engine\data\tile.xlsx')
        sheets = xlsx.sheets()
        print(sheets)
        sheet = xlsx.sheet_by_name('land')

        cell_info = sheet.cell(rowx=1, colx=1)
        print(cell_info)

if __name__ == "__main__":
    data = Data()
    data.xlsx()