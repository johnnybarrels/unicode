from app import db
from flask_login import UserMixin


enrolments = db.Table('enrolments',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.course_id'), primary_key=True)
)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    is_admin = db.Column(db.Boolean, nullable=False)
    courses = db.relationship('Course', secondary=enrolments, lazy='subquery',
                              backref=db.backref('users', lazy=True))

    def __repr__(self):   
        return '<User: {}>'.format(self.email)


class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True, nullable=False)
    course_name = db.Column(db.String(64))
    # admin_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    tests = db.relationship('Test', backref='course', lazy=True)

    def __repr__(self):
        return '<Course: {}>'.format(self.course_name)


class Test(db.Model):
    __tablename__ = 'tests'
    test_id = db.Column(db.Integer, primary_key=True, nullable=False)
    test_name = db.Column(db.String(64), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'))
    questions = db.relationship('Question', backref='test', lazy=True)

    def __repr__(self):
        return '<Test: {}>'.format(self.test_name)


class Question(db.Model):
    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_string = db.Column(db.String(256), nullable=False)
    answer = db.Column(db.String(256), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id'))
    mark_alloc = db.Column(db.Integer)
    question_group = db.Column(db.Integer)

    def __repr__(self):
        return '<Question: {}>'.format(self.question_string)


class Result(db.Model):
    __tablename__ = 'results' 
    result_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.test_id'), nullable = False)
    score = db.Column(db.Integer)
    is_marked = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Result {result}, User {user}, Test {test}, Score {score}>, Marked? {marked}'.format(result = self.result_id, user = self.user_id, test = self.test_id, score = self.score, marked = self.is_marked)


"""---------------------------------------------------------------------------------
# This is where we build our relational database
class User(db.Model):

    # Initialising basic user info
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True)
    email         = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin      = db.Column(db.Boolean(), nullable=False)

    courses = db.relationship('Course', backref='user', lazy='dynamic')

    # Printing out which user is current
    def __repr__(self):
        return f'<User {self.username}>'


class Course(db.Model):
    # Initialising basic course info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    tests = db.relationship('Test', backref='course', lazy='dynamic')

    # Printing out which Course is current
    def __repr__(self):
        return f'<Course {self.name}>'


class Test(db.Model):

    # Initialising basic course info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False) 

    questions = db.relationship('Question', backref='test', lazy='dynamic')

    # Printing out which Course is current
    def __repr__(self):
        return f'<Test {self.name}>'


class Question(db.Model):

    # Initialising basic course info
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('output', 'multi', 'write'))
    body = db.Column(db.String(500))
    solution = db.Column(db.String(100))

    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)

    # Printing out which Course is current
    def __repr__(self):
        return f'<Question {self.body}>'
---------------------------------------------------------------------------------------"""
