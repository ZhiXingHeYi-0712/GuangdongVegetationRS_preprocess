### 下载
在GEE_downloader项目：  
在main.py中调整是否下载和下载的时间范围。下载的文件存储在根目录下各文件夹。  
运行unzip_all.cmd  

### 预处理
将在GEE_downloader中下载的数据复制到data_month下
先运行clip_by_month.py, 结果在data_month_clip  
再运行reorganize_by_month.py，结果在reorganize_month  