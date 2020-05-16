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

CREATE TABLE question(
    question_id integer NOT NULL,
    question_string varchar(256) NOT NULL,
    answer varchar(256) NOT NULL,
    test_id integer,
    mark_alloc integer,
    question_group integer NOT NULL,
    PRIMARY KEY(question_id),
    FOREIGN KEY(test_id) REFERENCES test(test_id)
    ON DELETE SET NULL ON UPDATE NO ACTION
);
    

CREATE TABLE user (
    user_id integer NOT NULL,
    email varchar(32),
    password varchar(32),
    first_name varchar(32),
    last_name varchar(32),
    user_course integer,
    admin_yesno integer,
    PRIMARY KEY(user_id)
    FOREIGN KEY(user_course) REFERENCES course (course_id)
    ON DELETE SET NULL ON UPDATE NO ACTION
);

CREATE TABLE course (
    course_id integer NOT NULL,
    course_name varchar(32),
    PRIMARY KEY(course_id)
);
    
CREATE TABLE test (
    test_id integer NOT NULL,
    quiz_name varchar(32),
    course_id integer,
    PRIMARY KEY(test_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);
   

