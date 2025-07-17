# 使用官方Python基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 初始化数据库
RUN python -c "from app import db; db.create_all()"

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["flask", "run", "--host=0.0.0.0"]