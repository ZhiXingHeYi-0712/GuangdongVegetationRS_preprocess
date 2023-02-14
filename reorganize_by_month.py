import os
from osgeo import gdal
from utils import getDataLocationMonth
from pathlib import Path
import shutil
import numpy as np

roi = 'roi/guangdong_all.shp'

base_dir = 'reorganize_month'

month_list = [(i, j) for i in range(2001, 2021) for j in range(1, 13)]
climate_month_list = [(i, j) for i in range(2000, 2021) for j in range(1, 13)]

def getImageMetaData():
    standard_file = 'data_month/NDVI/2000_3.NDVI.tif'
    ds: gdal.Dataset = gdal.Open(standard_file, gdal.GA_ReadOnly)
    data: np.ndarray = ds.ReadAsArray()
    return data.shape

x, y = getImageMetaData()
# 每个月的数据包括：NDVI, LULC, pr, srad, tmmn, tmmx
# 气象数据不用每个月都存，直接存整个即可
data_length_per_month = 1 + 1 + 4

result_array = np.zeros((x, y, 240 + 240 + (252 * 4)), dtype='int32')
print(result_array.shape)
# 数据叠放方式：NDVI_1, NDVI_2, ... NDVI_240, LULC_1, LULC_2, ..., LULC_240, pr_1, pr_2, ..., pr_252, srad_1, ..., 
# srad_252, tmmn_1, ..., tmmn_252, tmmx_1, ..., tmmx_252
# 这里的下标表示：NDVI和LULC的下标表示第几月，从2001年1月开始算；其他气象数据的下标也表示第几月，但是从2000年1月开始算。这是为了方便考虑滞后效应。

z_index = 0
for var_type in ['NDVI', 'LULC']:
    print(var_type, z_index)
    for year, month in month_list:
        file_location, file_name = getDataLocationMonth(var_type, year, month)
        ds: gdal.Dataset = gdal.Open(file_location, gdal.GA_ReadOnly)
        data: np.ndarray = ds.ReadAsArray()

        result_array[:, :, z_index] = data
        z_index += 1

for var_type in ['pr', 'srad', 'tmmn', 'tmmx']:
    print(var_type, z_index)
    for year, month in climate_month_list:
        file_location, file_name = getDataLocationMonth(var_type, year, month)
        ds: gdal.Dataset = gdal.Open(file_location, gdal.GA_ReadOnly)
        data: np.ndarray = ds.ReadAsArray()

        result_array[:, :, z_index] = data
        z_index += 1

# 最后会输出一个npy文件，shape=(1183，1679，1488)，分别是（行数，列数，每个像元上的数据数）
np.save('reorganize_month/month_data.npy', result_array)

