from flask import url_for

def test_ping(client):
    res = client.get('/')
    print(res)
    assert res.status_code == 200
    assert str(res.get_data(),'utf-8') == 'Hello World DevOps'
