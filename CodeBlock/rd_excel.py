#coding:utf8
import xlrd

"""
book = xlrd.open_workbook('excel01.xlsx')
sheets = book.sheets()
print(sheets)
sheet = book.sheet_by_index(0)
print(sheet)
# 获取行、列
print(f"excel01.xlsx里有 {book.sheet_by_index(0).nrows} 行")
print(f"excel01.xlsx里有 {book.sheet_by_index(0).ncols} 列")

cell = sheet.cell(0, 0)
# 获取单元格的值
print(cell.value)
print('cell.ctype:%d' % cell.ctype)
print(xlrd.XL_CELL_TEXT)
print(sheet.ro)
"""
rbook = xlrd.open_workbook('excel01.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '总分', None)
for row in range(1, rsheet.nrows):
    rsheet.row_values(row, 1)

