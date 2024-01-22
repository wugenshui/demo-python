# FastAPI

## 本地调试

```bash
# 安装依赖
pip install "fastapi[all]"
# 本地启动，热重载
cd api; uvicorn fastApiDemo:app --reload --port 8000 --host localhost
```

## 服务端部署
```bash
pip install fastapi
pip install "uvicorn[standard]"
# 后台运行，生产环境不需要开启--reload
nohup uvicorn fastApiDemo:app --reload --port 8000 --host 0.0.0.0 &
```

# 安装依赖 
# 1. 
# 2. 服务端启动，热重载 
# 接口直接访问：http://localhost:8000/docs
