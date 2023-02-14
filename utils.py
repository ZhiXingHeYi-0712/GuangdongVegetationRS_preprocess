import os

def getDataLocation(data_type: str, year: int, month:int =-1):
    '''
    获取原始数据路径
    :param data_type: 数据类型，可选NDVI, NDVI_year_mean, pr, srad, tmmn, tmmx, lulc, 不区分大小写
    :return: (路径, 文件名)
    '''
    base_dir = 'data'

    data_type_string_lower = data_type.lower()

    if data_type_string_lower not in ['ndvi', 'ndvi_year_mean', 'pr', 'srad', 'tmmn', 'tmmx', 'lulc']:
        raise Exception('data type is not contained in predefined data type.')

    folder = {
        'ndvi': 'NDVI',
        'ndvi_year_mean': 'NDVI_year_mean',
        'pr': 'pr',
        'srad': 'srad',
        'tmmn': 'tmmn',
        'tmmx': 'tmmx',
        'lulc': 'LULC'
    }[data_type_string_lower]

    band = {
        'ndvi': 'NDVI',
        'ndvi_year_mean': 'NDVI',
        'pr': 'pr',
        'srad': 'srad',
        'tmmn': 'tmmn',
        'tmmx': 'tmmx',
        'lulc': 'LC_Type1'
    }[data_type_string_lower]


    if data_type_string_lower not in ['ndvi_year_mean', 'lulc']:
        # 月数据
        if month < 1 or month > 12:
            raise Exception('input month error, or month param is not given when the data type is a month data.')
        
        name = f'{year}_{month}.{band}.tif'
        dest = os.path.join(folder, name)

    if data_type_string_lower in ['ndvi_year_mean', 'lulc']:
        name = f'{year}.{band}.tif'
        dest = os.path.join(folder, name) 

    return (os.path.join(base_dir, dest), name)

def getDataLocationMonth(data_type: str, year: int, month:int =-1):
    '''
    获取原始数据路径
    :param data_type: 数据类型，可选NDVI, NDVI_year_mean, pr, srad, tmmn, tmmx, lulc, 不区分大小写
    :return: (路径, 文件名)
    '''
    base_dir = 'data_month'

    data_type_string_lower = data_type.lower()

    if data_type_string_lower not in ['ndvi', 'ndvi_year_mean', 'pr', 'srad', 'tmmn', 'tmmx', 'lulc']:
        raise Exception('data type is not contained in predefined data type.')

    folder = {
        'ndvi': 'NDVI',
        'ndvi_year_mean': 'NDVI_year_mean',
        'pr': 'pr',
        'srad': 'srad',
        'tmmn': 'tmmn',
        'tmmx': 'tmmx',
        'lulc': 'LULC'
    }[data_type_string_lower]

    band = {
        'ndvi': 'NDVI',
        'ndvi_year_mean': 'NDVI',
        'pr': 'pr',
        'srad': 'srad',
        'tmmn': 'tmmn',
        'tmmx': 'tmmx',
        'lulc': 'LC_Type1'
    }[data_type_string_lower]


    if data_type_string_lower not in ['ndvi_year_mean', 'lulc']:
        # 月数据
        if month < 1 or month > 12:
            raise Exception('input month error, or month param is not given when the data type is a month data.')
        
        name = f'{year}_{month}.{band}.tif'
        dest = os.path.join(folder, name)

    if data_type_string_lower in ['ndvi_year_mean', 'lulc']:
        name = f'{year}.{band}.tif'
        dest = os.path.join(folder, name) 

    return (os.path.join(base_dir, dest), name)
