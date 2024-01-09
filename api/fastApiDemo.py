from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}

@app.get("/info")
async def info():
    """
    项目信息
    :return:
    """
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# 服务端启动 pip install uvicorn
# nohup uvicorn fastApiDemo:app --reload --port 8000 --host 0.0.0.0 &
