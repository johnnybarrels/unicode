import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    return conn

# inputs: database connection object as conn, values to be inserted as n-tuple
# returns 
def create_question(conn, question):
    
    sql = '''INSERT INTO question (question_string, answer, test_id, mark_alloc, question_group)
                VALUES(?, ?, ?, ?, ?, ?) '''

    cur = conn.cursor()
    cur.execute(sql, question)

def main():

    db_file = 'unicode.db'

    conn = create_connection(db_file)

    with conn:
    
        question_1 = ('What is x', '3', 1, 4, 'output')

        create_question(conn, question_1)

if __name__ == '__main__':
    main()
