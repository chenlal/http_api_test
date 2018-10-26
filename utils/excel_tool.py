# coding=utf-8
import os

import xlwt
import xlrd
from config import config


class ExcelTool:

    def __init__(self, filename, sheet_id=0):
        self.filename = filename
        self.sheet_id = sheet_id

    def open_excel(self):
        return xlrd.open_workbook(self.filename)

    def get_sheet(self):
        return self.open_excel().sheets()[self.sheet_id]

    def get_row(self):
        return self.get_sheet().nrows

    def get_cell(self, row, colx):
        return self.get_sheet().cell(row, colx).value

    # def write_cell(self):


if __name__ == '__main__':
    et = ExcelTool(os.path.abspath('..') + "/testcase.xls")
    for i in range(1, et.get_row()):
        print(et.get_cell(i, config.EXPECT_CODE))
