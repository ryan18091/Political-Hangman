from src import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/login', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)

    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Please login', response.data)

if __name__ == '__main__':
    unittest.main()