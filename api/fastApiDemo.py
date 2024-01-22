from fastapi import FastAPI,Header
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    username: str
    password: str | None = None

app = FastAPI()

@app.get("/")
def index():
  return {"message": "Hello World"}

@app.get("/user/{id}")
def param(id, query: str = None):
  """
  获取路径参数、查询参数
  """
  return {"id": id, "query": query}

@app.get("/header")
def header(cookie=Header(None)):
  """
  获取 header 信息
  """
  return {"Cookie": cookie}

@app.post("/body")
def body(item: Item):
  """
  获取 Body 信息
  """
  return {"data":{"username":item.username,"password":item.password}}

@app.get("/info")
def info():
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
