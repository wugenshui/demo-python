cd vuepress2doc
# 批量安装依赖
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python index.py

# 将依赖包写入 requirements.txt
pip freeze > requirements.txt

# 单个依赖安装 
pip install pdfkit -i https://mirrors.aliyun.com/pypi/simple/
