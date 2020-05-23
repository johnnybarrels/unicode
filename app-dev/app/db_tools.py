from app import db
from app.models import User, Course, Test, Question, Result
from werkzeug.security import generate_password_hash


def clear_data():

    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Clear table {table}')
        db.session.execute(table.delete())
    db.session.commit()


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

    t1 = Test(id=1, name='2020 Final Exam', course_id=1, is_live=True)

    t2 = Test(id=2, name='2020 Mid sem DRAFT', course_id=1, is_live=False)

    t3 = Test(id=3, name='2020 Final Exam DRAFT', course_id=2)

    t4 = Test(id=4, name='2020 Mid sem', course_id=2)

    q1 = Question(id=1, question_string='What is the output of this function?',
                  code_string=r"def func(s):\n\tl = [c for c in s[::-1]]\n\t\tfor i in range(0, len(l), 2):\n\tif l[i].islower():\n\tl[i] = l[i].upper()\n\treturn ''.join(l)\nprint(func('Practice Question'))",
                  answer='NoItSeUQ eCiTcArP', test_id=1, mark_alloc=5,
                  question_type=1)

    q2 = Question(id=2, question_string='What data type is output from this code?',
                  code_string=r"def func2(x):\n\tif x == 1:\n\t\treturn 1\n\telse:\n\t\treturn (x * func2(x - 1))\n\n\nprint(func2(5.0))", answer='float', test_id=1, mark_alloc=3,
                  question_type=2, mcq_1='int', mcq_2='str',
                  mcq_3='float', mcq_4='bool')

    q3 = Question(id=3, question_type=3, test_id=1, mark_alloc=8,
                  question_string=r"Write a Python function.\n\nThe input string can contain any ASCII character.")

    db.session.add_all([u1, u2, t1, t2, t3, t4, q1, q2, q3])
    db.session.commit()


def purge_and_load():
    clear_data()
    load_data()