# Python環境宣言
FROM python:3.10

WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY . .

RUN pip install -r requirements.txt

# アプリの起動コマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]