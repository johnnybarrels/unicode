import unittest, os, time
from app import app, db
from app.models import User, Course, Question, Test, Result
from selenium import webdriver
basedir = os.path.abspath(os.path.dirname(__file__))

class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=os.path.join(basedir,'geckodriver'))
        if not self.driver:
            self.skiptest
        else:
            db.init_app(app)
            db.create_all()
            db.session.query(User).delete()
            #add other models in db
            u = User(id = 1, email='test@test.com', first_name='testfirst', last_name='testlast')
            u.set_password('pw')
            db.session.add(u)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000')


    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.query(User).delete()
            #add other models in db
            db.session.commit()
            db.session.remove()

    def test_login(self):
        self.driver.get('http://localhost:5000')
        time.sleep(1)
        email_field =  self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit_field = self.driver.find_element_by_id('login-btn')

        email_field.send_keys('test@test.com')
        password_field.send_keys('pw')
        submit_field.click()
        time.sleep(1)

        message =  self.driver.find_element_by_class_name('portal-msg').get_attribute('innerHTML')
        self.assertEqual(message, 'SELECT A COURSE TO VIEW TESTS / VIEW RESULTS')

if __name__=='__main__':
    unittest.main(verbosity=2)
