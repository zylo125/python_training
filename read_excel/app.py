from ast import Try
import xlwings as xw
import numpy as np
import os
import glob
import shutil
import re


def get_value():
    global sheet
    global af_last_raw
    global af_last_column
    global wb
    global af_list
    xw.App(visible=True)
    wb = xw.Book('./data.xlsx')
    sheet = wb.sheets['Sheet1']
    last_raw = sheet.range(1,1).end("right")
    last_column = sheet.range(1,1).end("down")
    #rng = wb.sheets[0].range('a1:f8')
    rng = sheet.range(last_raw, last_column)
    rng.api.AutoFilter(Field=4, Criteria1="common")
    af_last_raw = sheet.range(2,1).end("right")
    af_last_column = sheet.range(1,1).end("down")
    af_rng = sheet.range(af_last_raw, af_last_column)
    af_list = sheet.range(af_last_raw, af_last_column).value
    af_count = sheet.range(af_last_raw, af_last_column).count
get_value()

def create_dir():
    path = './'
    for index,item in enumerate(af_list):
        result = "-".join(item)
        os.mkdir(path + str(index + 1) + "NUM-" + result)
create_dir()

def file_sort():
    path = './'
    files = os.listdir(path)
    dir = [ f for f in files if os.path.isdir(os.path.join(path, f))]
    file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    print(file,"all files")
    print(dir, "all dir")
    for arr in af_list:
        for el in arr:
            try:
                l_in = [s for s in file if el in s]
                print(l_in, el, "FILES")
                d_in = [d for d in dir if el in d]
                print(d_in, el, "DIRS")
                if l_in and d_in:
                    print("BOUTH MATCH")
                    res_l = "".join(l_in)
                    print(res_l)
                    res_d = "".join(d_in)
                    print(res_d)
                    shutil.copy(res_l, res_d)
            except:
                print("NO MATCH")
file_sort()

nm_array = sheet.range(af_last_raw, af_last_column).options(np.array, expand='table').value
print(nm_array)

wb.close()
app = xw.apps.active 
app.kill()