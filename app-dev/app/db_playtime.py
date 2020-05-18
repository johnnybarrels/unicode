from app import db
from app.models import User, Course

u1 = User(id=25, email='student@test.com', first_name='Student', last_name='Test',
          password_hash='pbkdf2:sha256:150000$nfbYPHOa$b054a2c58abc670645958066b3d1ff702ffcb66dafb1c632566a5b4105d71480',
          is_admin=0)

u2 = User(id=10, email='admin@test.com', first_name='Admin', last_name='Test', 
          password_hash='pbkdf2:sha256:150000$nfbYPHOa$b054a2c58abc670645958066b3d1ff702ffcb66dafb1c632566a5b4105d71480',
          is_admin=1)

c5504 = Course(id=5504, course_name='Agile Web Development')

c1401 = Course(id=1401, course_name='Intro to Python')

u1.courses.append(c1401)
u2.courses.append(c5504)
u2.courses.append(c1401)


db.session.add_all([u1, u2])
