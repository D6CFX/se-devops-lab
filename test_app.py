import pytest
from app import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    # 改用字符串判断，或者把中文改成utf-8解码校验
    assert "DevOps 实验成功" in response.data.decode("utf-8")
