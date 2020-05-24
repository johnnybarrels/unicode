from app import db, login
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


enrolments = db.Table('enrolments',
                      db.Column('user_id', db.Integer, db.ForeignKey(
                          'users.id'), primary_key=True),
                      db.Column('course_id', db.Integer, db.ForeignKey(
                          'courses.id'), primary_key=True)
                      )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    # student_id = db.Column(db.Integer, index=True)
    courses = db.relationship('Course', secondary=enrolments, lazy='subquery',
                              backref=db.backref('users', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_users(course_id):
        course = Course.query.filter_by(id=course_id).first()
        course_enrolments = User.query.join(enrolments).join(
            Course).filter((enrolments.c.course_id == course.id)).all()
        return course_enrolments

    def __repr__(self):
        return f'<User: {self.email}>'


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64))
    course_code = db.Column(db.String(32))
    tests = db.relationship('Test', backref='course', lazy=True)

    def __repr__(self):
        return f'<Course: {self.name}>'


class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    is_live = db.Column(db.Boolean, nullable=False, default=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    questions = db.relationship('Question', backref='test', lazy=True)

    def get_user_submissions(self, user_id):
        return Submission.query.join(Question).join(Test).filter(
            (Submission.question_id == Question.id)
            & (Question.test_id == self.id)
            & (Submission.user_id == user_id)).all()

    def __repr__(self):
        return f'<Test: {self.name}>'


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_string = db.Column(db.String(256), nullable=False)
    code_string = db.Column(db.String(1024))
    answer = db.Column(db.String(256))
    mcq_1 = db.Column(db.String(128))
    mcq_2 = db.Column(db.String(128))
    mcq_3 = db.Column(db.String(128))
    mcq_4 = db.Column(db.String(128))
    mcq_answer = db.Column(db.String(8))
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    mark_alloc = db.Column(db.Integer, nullable=False)
    # 1 = Output, 2 = MCQ, 3 = Write code
    question_type = db.Column(db.Integer, nullable=False, default=1)

    def get_mcq_options(self):
        return [self.mcq_1, self.mcq_2, self.mcq_3, self.mcq_4]

    def get_user_submission(self, user_id):
        return Submission.query.join(Question).filter(
            (Submission.question_id == self.id)
            & (Submission.user_id == user_id)).first()

    def __repr__(self):
        return f'<Question: {self.question_string}>'


class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    output_sub = db.Column(db.String(128))
    mcq_sub = db.Column(db.String(8))
    code_sub = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return f'<Submission: User ID: {self.user_id}, Question ID: {self.question_id}>'


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)
    score = db.Column(db.Integer)
    is_marked = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Result {self.result_id}, User{self.user_id}, Test {self.test_id}, Score: {self.score}, Marked? {self.is_marked}'
