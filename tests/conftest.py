import pytest
from app import create_app


@pytest.fixture
def app():
    # 创建测试应用实例
    app = create_app()
    app.config['TESTING'] = True
    return app

# 替换旧的 _request_ctx_stack 使用
@pytest.fixture
def client(app):
    with app.test_request_context():
        yield app.test_client()