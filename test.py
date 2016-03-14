from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #Ensure that flask was properly set up
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login',content_type='html/text')
        self.assertEqual(response.status_code,200)

    #Ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login',content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    #Ensure login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin",password="admin"),
            follow_redirects = True
        )
        self.assertIn(b'You were just logged in' , response.data)


    #Ensure login behaves incorrectly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="blah" , password="admin"),
            follow_redirects = True
        )
        self.assertIn(b'Invalid credentials. Please try again', response.data) 
        

    #Ensure logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="admin",password="admin"),
            follow_redirects = True
        )
        #test fails if follow_redirects=False
        response = tester.get('/logout', follow_redirects = True )
        self.assertIn(b'You were just logged out' , response.data)

    #Need to have test as the prefix for each function
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first' in response.data)

    def test_logout_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first', response.data)

    #ensure posts show p on main page
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin",password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hello from', response.data)

if __name__ == "__main__":
    unittest.main()