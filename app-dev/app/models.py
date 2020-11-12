from app import db, login
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from statistics import stdev

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
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    courses = db.relationship('Course', secondary=enrolments, lazy='subquery',
                              backref=db.backref('users', lazy=True))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_test_submissions(self, test_id):
        return Submission.query.join(User).filter(
            (Submission.user_id == self.id) &
            (Submission.test_id == test_id)
        ).all()

    def get_result(self, test_id):
        return Result.query.filter_by(user_id=self.id, test_id=test_id).first()

    def has_submitted(self, test_id):
        return self.get_result(test_id) is not None

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<User: {self.email}>'


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64))
    course_code = db.Column(db.String(32))
    tests = db.relationship('Test', backref='course', lazy=True)

    def get_num_enrolments(self):
        students = []
        for user in self.get_users():
            if not user.is_admin:
                students.append(user)
       
        return len(students)            

    def get_users(self):
        return User.query.join(enrolments).join(Course).filter(
            enrolments.c.course_id == self.id).all()

    def __repr__(self):
        return f'<Course: {self.name}>'


class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    is_live = db.Column(db.Boolean, nullable=False, default=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    questions = db.relationship('Question', backref='test', lazy=True)

    def total_marks(self):
        total = sum((question.mark_alloc for question in self.questions))
        
        if total:
            return total
        else:
            return 1

    def get_std_dev(self):
        all_res = self.get_test_results()
        marks = []        

        for res in all_res:
            marks.append(res.score)

        if len(marks) > 1:
            return round(stdev(marks), 2)            
        else:
            return 0

    def get_average_mark(self):
        all_res = self.get_test_results()
        total = 0

        for res in all_res:
            total += res.score
        print(total)
        print(self.total_marks())
        return round((total / max(len(all_res), 1)) / self.total_marks() * 100, 2)

    def get_max_mark(self):
        all_res = self.get_test_results()
        all_res.sort(key=lambda r: r.score, reverse=True)

        if all_res:
            return round((all_res[0].score) / self.total_marks() * 100, 2)
        else:
            return 0

    def get_min_mark(self):
        all_res = self.get_test_results()
        all_res.sort(key=lambda r: r.score)

        if all_res:
            return round(all_res[0].score / self.total_marks() * 100, 2)
        else:
            return 0

    def get_num_results(self):
        return len(self.get_test_results())

    def get_submitted_users(self):
        return User.query.join(Submission).join(Test).filter(
            Submission.test_id == self.id).all()

    def get_user_submissions(self, user_id):
        return Submission.query.join(Test).filter(
            (Submission.test_id == self.id)
            & (Submission.user_id == user_id)).all()

    def get_all_submissions(self):
        return Submission.query.join(Test).filter(
            Submission.test_id == self.id).all()

    def has_result(self, user_id):
        return Result.query.filter_by(user_id=user_id, test_id=self.id).first()

    def get_test_results(self):
        return Result.query.filter_by(test_id=self.id).all()

    def get_student_result(self, user_id):
        return Result.query.filter_by(test_id=self.id, user_id=user_id).first()

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
    submissions = db.relationship('Submission', backref='question', lazy=True)

    def get_mcq_options(self):
        return [self.mcq_1, self.mcq_2, self.mcq_3, self.mcq_4]

    def get_user_submission(self, user_id):
        return Submission.query.join(Question).filter(
            (Submission.question_id == self.id)
            & (Submission.user_id == user_id)).first()

    def get_all_submissions(self):
        return Submission.query.join(Question).filter(
            Submission.question_id == self.id).all()

    def __repr__(self):
        return f'<Question: {self.question_string}>'


class Submission(db.Model):
    __tablename__ = 'submissions'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    output_sub = db.Column(db.String(128))
    mcq_sub = db.Column(db.String(8))
    code_sub = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    score = db.Column(db.Integer, default=0)
    needs_marking = db.Column(db.Boolean, nullable=False, default=True)

    def auto_mark(self):
        q = Question.query.filter_by(id=self.question_id).first()
        if q.question_type == 1:
            if self.output_sub == q.answer:
                self.score = q.mark_alloc
            self.needs_marking = False

        elif q.question_type == 2:
            if self.mcq_sub == q.mcq_answer:
                self.score = q.mark_alloc
            self.needs_marking = False

        db.session.commit()

    def get_question(self):
        return Question.query.filter_by(id=self.question_id).first()

    def get_result(self):
        return Result.query.filter_by()

    def __repr__(self):
        return f'<Submission: User ID: {self.user_id}, Question ID: {self.question_id}>'


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)
    score = db.Column(db.Integer)
    needs_marking = db.Column(db.Boolean, nullable=False, default=True)
    feedback = db.Column(db.String(1024))

    def get_mark(user_id, test_id):
        return Result.query.filter((user_id == user_id)&(test_id == test_id)).first().score


    def __repr__(self):
        return f'<Result {self.id}, User{self.user_id}, Test {self.test_id}, Score: {self.score}>'
