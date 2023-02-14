### 下载
在GuangdongVegetationRS_getData项目：  
在main.py中调整是否下载和下载的时间范围。下载的文件存储在根目录下各文件夹。  
运行unzip_all.cmd  

### 年预处理
将在GuangdongVegetationRS_getData中下载的数据复制到GuangdongVegetationRS_preprocess/data下  
先运行reorganize_by_year.py, 结果输出到reorganize_year/年份下  
再运行reorganize_by_year2.py，结果输出到reorganize_year/numpy下

### 月预处理
将在GuangdongVegetationRS_getData中下载的数据复制到GuangdongVegetationRS_preprocess/data_month下
先运行clip_by_month.py, 结果在data_month_clip  
再运行reorganize_by_month.py，结果在reorganize_month  