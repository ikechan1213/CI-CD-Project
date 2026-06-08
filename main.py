from fastapi import FastAPI

app = FastAPI()

# GETリクエストで / にアクセスされたときの処理
@app.get("/")
def read_root():
    return {"message": "CICD成功!だよーーん"}

@app.get("/hello")
def read_hello():
    return {"message": "Helloo, World"}