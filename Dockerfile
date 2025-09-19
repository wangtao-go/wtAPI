# 基础镜像
FROM docker.xuanyuan.me/continuumio/miniconda

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动命令（开发模式可以使用自动重载）
CMD ["uwsgi", "--ini", "uwsgi.ini", "--py-auto-reload=2"]

