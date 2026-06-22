#コンテナ土台Python 3.12 が入っている軽量なLinux環境を使う
FROM python:3.12-slim

#コンテナ内の作業場所を決める命令
WORKDIR /app

#コンテナ内にローカルのファイルをコピーする命令
#自分のPC側にある requirements.txt を、コンテナ内の /app/ にコピーする
COPY requirements.txt /app/

#コンテナを作る途中でコマンドを実行する命令
#requirements.txt に書いてあるPythonライブラリをインストールする
RUN pip install --no-cache-dir -r requirements.txt

#プロジェクト全体をコンテナにコピーする命令
#今いるフォルダの中身を、コンテナ内の /app/ にコピーする
COPY . /app/

#コンテナが起動したときに実行するコマンド
#コンテナを起動したら、Djangoの開発サーバーを起動する
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]