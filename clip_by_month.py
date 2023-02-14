import os
from osgeo import gdal
from utils import getDataLocationMonth
from pathlib import Path
import shutil

roi = 'roi/guangdong_all.shp'

def clipRasterByRoi(input_raster, output_raster):
    gdal.Warp(output_raster, input_raster, format='GTiff', cutlineDSName=roi, dstNodata=-9999)

input_dir = 'data_month'
output_dir = 'data_month_clip'

for var_type in ['LULC', 'NDVI', 'pr', 'srad', 'tmmn', 'tmmx']:
    os.mkdir(os.path.join(output_dir, var_type))
    file_list = os.listdir(os.path.join(input_dir, var_type))
    for file in file_list:
        clipRasterByRoi(os.path.join(input_dir, var_type, file), os.path.join(output_dir, var_type, file))


