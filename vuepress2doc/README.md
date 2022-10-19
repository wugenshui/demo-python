# 运行说明

## 安装依赖组件
https://wkhtmltopdf.org/downloads.html

## 批量安装依赖
cd vuepress2doc
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python index.py

## 其它

### 将依赖包写入 requirements.txt
pip freeze > requirements.txt

### 单个依赖安装 
pip install pdfkit -i https://mirrors.aliyun.com/pypi/simple/
pip install requests -i https://mirrors.aliyun.com/pypi/simple/
pip install beautifulsoup4 -i https://mirrors.aliyun.com/pypi/simple/

### 参考文档
https://segmentfault.com/a/1190000019132150
