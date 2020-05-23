import unittest, os
from app import app, db
from app.models import User, Course, Question, Test, Result

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() #create a virtual env to run test
        #make sure data base is empty
        db.create_all()
        u = User(id = 1, email='test@test.com', first_name='testfirst', last_name='testlast' )
        db.session.add(u)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

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

    def test_test_creation(sef):
        

if __name__=='__main__':
    unittest.main(verbosity=2)
