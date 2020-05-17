from app import db
from app.models import User, Course

jb = User(id=25, email='johnny@barrels.com', first_name='Johnny',
          password_hash='pbkdf2:sha256:150000$nfbYPHOa$b054a2c58abc670645958066b3d1ff702ffcb66dafb1c632566a5b4105d71480',
          last_name='Barrett', is_admin=0)

tim = User(id=10, email='tim@french.com', first_name='Tim',
          password_hash='pbkdf2:sha256:150000$nfbYPHOa$b054a2c58abc670645958066b3d1ff702ffcb66dafb1c632566a5b4105d71480',
          last_name='French', is_admin=1)

c5504 = Course(id=5504, course_name='Agile Web Development')

c1401 = Course(id=1401, course_name='Intro to Python')

jb.courses.append(c1401)
tim.courses.append(c5504)

db.session.add_all([jb, tim])
