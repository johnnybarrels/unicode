import unittest, os
from app import app, db
from app.models import User, Course, Question, Test, Result
from config import Config, TestConfig

class UserModelTest(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client() #create a virtual env to run test
        #make sure data base is empty
        app.config.from_object(TestConfig)
        db.init_app(app)
        db.session.rollback()
        db.create_all()
        u = User(id = 1, email='test@test.com', first_name='testfirst', last_name='testlast' )
        admin = User(id = 2, email = 'admin@admin.com', first_name = 'admin', last_name='admin')
        test = Test(id = 1, name = 'test', is_live = 'True')
        course = Course(id = 1, name='agile', course_code = 'CITS5504')
        db.session.add(u)
        db.session.add(admin)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    ########################
    #### helper methods ####
    ########################

    
    def register(self, first_name, last_name, email, password, password_again):
        return self.app.post('/register', data=dict(first_name=first_name, last_name=last_name, email=email,  password=password, password_again=password_again),
follow_redirects=True)
 
    def login(self, email, password):
        return self.app.post('/index', data=dict(email=email, password=password), follow_redirects=True)

    ###############
    #### tests ####
    ###############


    def test_set_pw(self):
        u = User.query.get(1)
        u.set_password('pwd')
        self.assertFalse(u.check_password('passw0rd'))
        self.assertTrue(u.check_password('pwd'))

    def test_set_pw2(self):
        u = User.query.get(1)
        u.set_password('pwd2')
        self.assertFalse(u.check_password('pwd'))
        self.assertTrue(u.check_password('pwd2'))

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_users_can_register(self):
        new_user = User(id = 4, email='test4@test.com', first_name='test4first', last_name='test4last' )
        new_user.set_password('pw')
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.first_name
        assert t.first_name == "test4first"

    def test_valid_user_registration(self):
        response = self.register('robot', 'test', 'robot@test.com', 'robot', 'robot')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have registered', response.data)

    def test_users_cannot_login_unless_registered(self):
        signin = self.login('foo@bar.com', 'bar')
        self.assertEqual(signin.status_code, 200)
        self.assertIn(b'Invalid username or password', signin.data)

    def test_duplicate_user_registeration_throws_error(self):
        self.register('test', 'test', 'fletcher@realpython.com', 'python101', 'python101')
        response = self.register('test', 'test', 'fletcher@realpython.com', 'python101', 'python101')
        self.assertIn(b'Email is already registered!', response.data)



if __name__=='__main__':
    unittest.main(verbosity=2)
