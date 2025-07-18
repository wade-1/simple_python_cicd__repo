from app import create_app, db
import os

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()
    print("Database initialized.")

# 检查数据库是否已初始化
def check_database_initialized():
    db_file = os.path.join(app.instance_path, 'employees.db')
    return os.path.exists(db_file)

if __name__ == '__main__':
    # 如果数据库不存在，则初始化
    if not check_database_initialized():
        print("Initializing database...")
        with app.app_context():
            db.create_all()
    
    # 关键修改：指定监听所有网络接口
    app.run(host='0.0.0.0', port=5000)