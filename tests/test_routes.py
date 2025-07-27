def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    # 使用 response.text 获取解码后的字符串
    assert '员工列表' in response.text

def test_add_employee(client):
    response = client.post('/add', data={
        'name': '张三',
        'position': '工程师',
        'department': '技术部'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert '张三' in response.text