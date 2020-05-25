import unittest, os, time
from app import app, db
from app.models import User, Course, Question, Test, Result
from selenium import webdriver
from config import Config, TestConfig

basedir = os.path.abspath(os.path.dirname(__file__))

class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=os.path.join(basedir,'geckodriver'))

        if not self.driver:
            self.skiptest
        else:
            db.create_all()
            db.session.query(User).delete()
            #add other models in db
            u = User(id = 1, email='test@test.com', first_name='testfirst', last_name='testlast')
            admin = User(id = 1111, email='admin@test.com', first_name='admintest', last_name='admintest', is_admin = True)
            u.set_password('pw')
            admin.set_password('pw')
            db.session.add(u)
            db.session.add(admin)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000')


    def tearDown(self):
        if self.driver:
            self.driver.close()
            #add other models in db
            db.session.commit()
            db.session.remove()
         

    def test_login_user(self):
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

    def test_login_admin(self):
        self.driver.get('http://localhost:5000')
        time.sleep(1)
        email_field =  self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        submit_field = self.driver.find_element_by_id('login-btn')

        email_field.send_keys('admin@test.com')
        password_field.send_keys('pw')
        submit_field.click()
        time.sleep(1)

        message =  self.driver.find_element_by_class_name('portal-msg').get_attribute('innerHTML')
        self.assertEqual(message, 'SELECT A COURSE TO CREATE A NEW TEST / VIEW RESULTS')

    def test_user_registration(self):
        self.driver.get('http://localhost:5000/register')
        time.sleep(3)

        first_name_field = self.driver.find_element_by_id('first_name')
        last_name_field = self.driver.find_element_by_id('last_name')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        password_again_field = self.driver.find_element_by_id('password_again')
        registration_field = self.driver.find_element_by_id('login-btn')

        first_name_field.send_keys('robot_test')
        last_name_field.send_keys('robot_test_last')
        email_field.send_keys('robot_test@test.com')
        password_field.send_keys('pw')
        password_again_field.send_keys('pw')
        time.sleep(1)
        registration_field.click()
        time.sleep(2)

        new_email_field =  self.driver.find_element_by_id('email')
        new_password_field = self.driver.find_element_by_id('password')
        new_submit_field = self.driver.find_element_by_id('login-btn')

        new_email_field.send_keys('robot_test@test.com')
        new_password_field.send_keys('pw')
        new_submit_field.click()
        time.sleep(2)

        message =  self.driver.find_element_by_class_name('portal-msg').get_attribute('innerHTML')
        self.assertEqual(message, 'SELECT A COURSE TO VIEW TESTS / VIEW RESULTS')

if __name__=='__main__':
    unittest.main(verbosity=2)
