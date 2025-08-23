FROM python:3.11.13-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムの更新と必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージのインストール
RUN pip install --no-cache-dir numpy

# プロジェクトファイルをコピー
COPY . .

# Python環境の設定
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# デフォルトコマンド
CMD ["bash"]
