import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # 创建Flask应用实例
    app = Flask(__name__, instance_relative_config=True)
    
    # 配置应用
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'employees.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # 初始化扩展
    db.init_app(app)
    
    # 注册蓝图
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app