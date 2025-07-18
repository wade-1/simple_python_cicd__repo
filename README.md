# 员工管理系统 - Flask应用

这是一个简单的员工管理系统，使用Flask框架开发，支持DevOps全流程自动化。

## 功能
- 查看员工列表
- 添加新员工
- 自动部署到Docker

## 开发环境设置
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt

# 初始化数据库
python init_db.py

# 运行应用
python wsgi.py