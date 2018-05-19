from flask import jsonify
class TestUser:
  def test_invalid_signup(self, client):
    response = client.post('/api/user/signup')
    assert response.status_code == 400

  def test_successful_signup(self, client):
    data = {
      'username': 'purpose',
      'password': 'password'
    }
    response = client.post('/api/user/signup', data)
    assert response.status_code == 200

