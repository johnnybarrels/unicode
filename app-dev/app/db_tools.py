from app import db
from app.models import User
from werkzeug.security import generate_password_hash


def clear_data():

    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Clear table {table}')
        db.session.execute(table.delete())
    db.session.commit()


def load_admins():

    u1 = User(id=1, email='tim@french.com', first_name='Tim', last_name='French',
              password_hash=generate_password_hash('password'),
              is_admin=1)

    u2 = User(id=2, email='tom@smoker.com', first_name='Tom', last_name='Smoker',
              password_hash=generate_password_hash('password'),
              is_admin=1)

    u3 = User(id=3, email='haolin@wu.com', first_name='Haolin', last_name='Wu',
              password_hash=generate_password_hash('password'),
              is_admin=1)

    db.session.add_all([u1, u2, u3])
    db.session.commit()


def purge_and_load():
    clear_data()
    load_admins()
