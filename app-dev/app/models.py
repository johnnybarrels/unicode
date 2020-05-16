from app import db


class Result(db.Model):

    result_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable = False)
    test_id = db.Column(db.Integer, nullable = False)
    score = db.Column(db.Integer)
    marked_yesno = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r %r %r>' % self.result_id

"""
CREATE TABLE result(
    result_id integer NOT NULL,
    user_id integer,
    test_id integer,
    score integer,
    marked_yesno integer,
    PRIMARY KEY(result_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id)
    ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(test_id) REFERENCES test(test_id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);
"""

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



