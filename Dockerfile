# 基础镜像
FROM docker.xuanyuan.me/continuumio/miniconda

# 设置工作目录
WORKDIR /app

# 安装R及相关系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        less \
        r-base \
        libssl-dev \
        libcurl4-openssl-dev \
        libxml2-dev \
        zlib1g-dev && \
    # 使用清华镜像加速R包安装
    Rscript -e "install.packages(c('openxlsx','data.table','lubridate','R.utils'), repos='https://mirrors.tuna.tsinghua.edu.cn/CRAN/')" \

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动命令（开发模式可以使用自动重载）
CMD ["uwsgi", "--ini", "uwsgi.ini", "--py-auto-reload=2"]

