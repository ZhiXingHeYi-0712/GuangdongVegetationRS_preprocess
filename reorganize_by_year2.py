# step 2
import os
from tkinter.messagebox import NO
import numpy as np
from osgeo import gdal

base_dir = 'reorganize_year'
NODATA = -9999
def reorganizeYearFolder(year: int):
    major_folder = os.path.join(base_dir, str(year))

    def aggregation(var_type: str) -> np.ndarray:
        # 聚合年内各月
        file_list = [os.path.join(major_folder, f'{year}_{month}.{var_type}.tif') for month in range(1, 13)]

        first_file = True
        data = np.ndarray([])
        for file in file_list:
            ds: gdal.Dataset = gdal.Open(file, gdal.GA_ReadOnly)
            if first_file:
                data: np.ndarray = ds.ReadAsArray()
                first_file = False
            else:
                data: np.ndarray = data + ds.ReadAsArray()
        return data
    
    # 聚合月数据
    pr = aggregation('pr')
    srad = aggregation('srad')
    tmmn = aggregation('tmmn')
    tmmx = aggregation('tmmx')

    # 不需要聚合的数据
    NDVI: np.ndarray = gdal.Open(os.path.join(major_folder, f'{year}.NDVI.tif')).ReadAsArray()
    LUCC: np.ndarray = gdal.Open(os.path.join(major_folder, f'{year}.LC_Type1.tif')).ReadAsArray()

    if not (pr.shape == srad.shape == tmmn.shape == tmmx.shape == NDVI.shape == LUCC.shape):
        raise Exception('Size is not compatible')

    # 通过数据尺寸检验
    NDVI_new = NDVI[NDVI != NODATA]
    data: np.ndarray = np.zeros((6, len(NDVI_new)))
    data[0] = NDVI_new
    data[1] = LUCC[LUCC != NODATA]

    # 聚合后的NODATA是-9999*12
    data[2] = pr[pr > NODATA]
    data[3] = srad[srad > NODATA]
    data[4] = tmmn[tmmn > NODATA]
    data[5] = tmmx[tmmx > NODATA]

    return data.astype('int32').T

for year in range(2001, 2021):
    data = reorganizeYearFolder(year)
    np.save(f'reorganize_year/numpy/{year}.npy', data)

