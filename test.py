import requests
import unittest


class TestLogin(unittest.TestCase):
    '''
    Before running this test module please create following user using
    MongoDB console:
        + username: vahid
        + password: test
    '''
    def test_password_reset(self):
        r = requests.post(
            'http://localhost:4000/user/reset_password',
            data={
                'username': 'vahid',
                'password': 'newpass'
            }
        )
  
    def test_login_success(self):
        r = requests.post(
            'http://localhost:4000/user/login',
            data={
                'username': 'vahid',
                'password': 'test'
            }
        )
        self.assertEqual('', r.json()['err'])

    def test_login_wrong_username(self):
        r = requests.post(
            'http://localhost:4000/user/login',
            data={
                'username': 'majid',
                'password': 'test'
            }
        )
        self.assertEqual(404, r.status_code)

    def test_login_wrong_password(self):
        r = requests.post(
            'http://localhost:4000/user/login',
            data={
                'username': 'vahid',
                'password': 'wrong password'
            }
        )
        self.assertEqual(404, r.status_code)


if __name__ == '__main__':
    unittest.main()
