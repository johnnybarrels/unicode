from app import app, db
from app.models import User, Course, Test, Question, Result


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Course': Course,
            'Test': Test, 'Question': Question, 'Result': Result}
