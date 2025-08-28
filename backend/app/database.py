import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://quizuser:quizpass@db:3306/quizdb"

Base = declarative_base()

# リトライ付きでエンジン作成
max_tries = 10
for i in range(max_tries):
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        break
    except OperationalError:
        print(f"DB接続失敗、再試行中... ({i+1}/{max_tries})")
        time.sleep(3)
else:
    raise Exception("DBに接続できませんでした")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
