def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'员工列表' in response.data

def test_add_employee(client):
    response = client.post('/add', data={
        'name': '张三',
        'position': '工程师',
        'department': '技术部'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'张三' in response.data