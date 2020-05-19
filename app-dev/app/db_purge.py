from app import db
from app.models import User, Course

users = User.query.all()
for u in users:
    db.session.delete(u)

courses = Course.query.all()
for c in courses:
    db.session.delete(c)
    