import xlrd
import json


def read_excel():
    # 打开excel文件
    workbook = xlrd.open_workbook('./excel01.xlsx')

    # 获取全部工作表(sheet)以及选取对应的工作表
    sheet_name = workbook.sheet_names()[0]
    host_sheet = workbook.sheet_by_name(sheet_name)

    # 获取工作表总行数
    rows = host_sheet.nrows
    return host_sheet, rows


# 选取数据
def read_data(host_sheet, rows):
    host_data = []  # 定义一个空列表用来存数据
    for row in range(rows):
        host_data += [host_sheet.row_values(row, 1)]
    # return host_data[1:]  # 从1开始(不要第一行表头)
    return host_data

if __name__ == '__main__':
    host_sheet1, rows1 = read_excel()
    host_datas = read_data(host_sheet1, rows1)
    # 转换成JSON
    # json_data_0 = json.dumps(host_datas[1], indent=2, ensure_ascii=False)
    # print(host_datas)
    # print(type(json_data_0))
    # print(json_data_0)

    # 使用zip将list转为json
    # print(zip(host_datas))
    # dict_host_datas = dict(zip(host_datas[0], host_datas[1]))
    # print(dict_host_datas)

    # 循环读取每一行，使用zip将list转为json
    # for i in
    for i in range(1, rows1):
        dict_host_datas = dict(zip(host_datas[0], host_datas[i]))
        print(dict_host_datas)

    print('--------------')
    # 替换掉json里面的value
    dict_host_datas = dict(zip(host_datas[0], host_datas[1]))  # 字典
    print(type(dict_host_datas))
    json_data = json.dumps(dict_host_datas, ensure_ascii=False)  # json
    print(f"type(json_data):{type(json_data)}, json_data:{json_data}")
    if isinstance(dict_host_datas, dict):  # 判断是否为字典类型实例
        for key in dict_host_datas:
            if key == '语文':
                dict_host_datas[key] = '11'
            if key == '数学':
                dict_host_datas[key] = '22'
            if key == '外语':
                dict_host_datas[key] = '33'
    print(dict_host_datas)

