# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=run.py

# 创建工作目录并设置为工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libmariadb-dev-compat && \
    rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建静态文件目录并设置权限
RUN mkdir -p /app/app/static && \
    chmod -R 755 /app/app/static

# 暴露端口
EXPOSE 5000

# 设置启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app", "--workers", "4", "--timeout", "120"]