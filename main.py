from fastapi import FastAPI

app = FastAPI()

# GETリクエストで / にアクセスされたときの処理
@app.get("/")
def read_root():
    return {"message": "CICD成功!してるよ～"}