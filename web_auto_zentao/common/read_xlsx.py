# -*- coding: utf-8 -*-
import xlrd


class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        # 打开这个路径下的文档
        self.data = xlrd.open_workbook(excelPath)
        # 选择sheet页
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)

        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                print(values)
                for x in range(self.colNum):
                    # 添加键值对
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    p = "D:\\BaiduNetdiskDownload\\zentao.xlsx"
    n = "Sheet1"
    data = ExcelUtil(p, n)
    print(data.dict_data())
