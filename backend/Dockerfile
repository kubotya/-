FROM python:3.9-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y libmariadb-dev-compat libmariadb-dev build-essential libssl-dev libffi-dev python3-dev

# 必要な Python パッケージをインストール
RUN pip install --no-cache-dir cryptography pymysql sqlalchemy uvicorn fastapi

# 作業ディレクトリ設定
WORKDIR /app

# アプリケーションのコードをコピー
COPY . /app

# アプリケーションを実行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
