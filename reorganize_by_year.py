import os
from osgeo import gdal
from utils import getDataLocation
from pathlib import Path
import shutil

roi = 'roi/guangdong_all.shp'

def clipRasterByRoi(input_raster, output_raster):
    gdal.Warp(output_raster, input_raster, format='GTiff', cutlineDSName=roi, dstNodata=-9999)

def reorganizeYear(year):
    base_dir = 'reorganize_year'

    base_year_dir = os.path.join(base_dir, str(year))

    if Path(base_year_dir).exists() and Path(base_year_dir).is_dir():
        # 已有则删除
        shutil.rmtree(base_year_dir)

    os.mkdir(base_year_dir)

    # 空文件夹，路径为base_year_dir

    # 处理NDVI
    ndvi_location, ndvi_file_name = getDataLocation('NDVI_year_mean', year)
    clipRasterByRoi(ndvi_location, os.path.join(base_year_dir, ndvi_file_name))

    # 处理LULC
    lulc_location, lulc_file_name = getDataLocation('LULC', year)
    clipRasterByRoi(lulc_location, os.path.join(base_year_dir, lulc_file_name))

    # 处理年降水、气温、辐射
    for month in range(1, 13):
        pr_location, pr_file_name = getDataLocation('pr', year, month)
        srad_location, srad_file_name = getDataLocation('srad', year, month)
        tmmn_location, tmmn_file_name = getDataLocation('tmmn', year, month)
        tmmx_location, tmmx_file_name = getDataLocation('tmmx', year, month)

        clipRasterByRoi(pr_location,   os.path.join(base_year_dir, pr_file_name))
        clipRasterByRoi(srad_location, os.path.join(base_year_dir, srad_file_name))
        clipRasterByRoi(tmmn_location, os.path.join(base_year_dir, tmmn_file_name))
        clipRasterByRoi(tmmx_location, os.path.join(base_year_dir, tmmx_file_name))

for year in range(2001, 2021):
    reorganizeYear(year)
