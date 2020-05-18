from app import db
from app.models import User, Course, Test, Result
from werkzeug.security import generate_password_hash


def load_data():
    u1 = User(id=25, email='student@test.com', first_name='Student', last_name='Test',
              password_hash=generate_password_hash('password'),
              is_admin=0)

    u2 = User(id=10, email='admin@test.com', first_name='Admin', last_name='Test',
              password_hash=generate_password_hash('password'),
              is_admin=1)

    c5504 = Course(id=1, course_code='CITS5504',
                   name='Agile Web Development')

    c1401 = Course(id=2, course_code='CITS1401', name='Intro to Python')

    u1.courses.append(c1401)
    u2.courses.append(c5504)
    u2.courses.append(c1401)

    t1 = Test(id=1, name='2020 Final Exam', course_id=1)

    t2 = Test(id=2, name='2020 Mid sem DRAFT', course_id=1)

    t3 = Test(id=3, name='2020 Final Exam DRAFT', course_id=2)

    t4 = Test(id=4, name='2020 Mid sem', course_id=2)

    db.session.add_all([u1, u2, t1, t2, t3, t4])
