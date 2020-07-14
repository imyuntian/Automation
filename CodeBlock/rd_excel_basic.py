import xlrd

# 获取工作簿
rbook = xlrd.open_workbook('excel01.xlsx')
# 获取工作簿里的sheet页
rsheet = rbook.sheet_by_index(0)
# 获取行值：读行1，从头开始读
row_values_0 = rsheet.row_values(1)
print(row_values_0)
# 获取行值：读行1，从第2个值开始读
row_values = rsheet.row_values(1, 1)
print(row_values)
print(sum(row_values))
# 获取列值
col_values = rsheet.col_values(0, 0)
print(col_values)
# 获取单元格的值
cell_value = rsheet.cell_value(1, 1)
print(cell_value)

"""
1.导入xlrd包
2.打开excel文件
3.获取全部工作表(sheet)
4.选取对应的工作表
5.选取所需数据
"""
# 获取所有sheet
names = rbook.sheet_names()
print(names)
# 获取某个sheet
name = rbook.sheet_names()[0]
print(name)

# 根据名字获取对应sheet
sheet2 = rbook.sheet_by_name('Sheet2')
print(sheet2.nrows, sheet2.ncols)
print(sheet2.cell_value(1, 1))
print(sheet2.cell_value(3, 2))
