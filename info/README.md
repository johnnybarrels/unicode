# **How to Use**

### For Admin(Teachers) Profile:
<details>
  <summary markdown="span">Instructions for admin, click me to expand</summary>
    
  - *_Create a New Course_*: 
    - Click on `CREATE A NEW COURSE` or "+" icon next to Course
    - Type Course Name
    - Type Course Code
    - Click `Create Course`
     
  - *_Create a New Test_*: 
    - Select the Course on the left panel
    - Click on `New Test`
    - Type Test name
    - Click `Create Test`
    - Click on the new created test
      - (Optional) Click on dropdown to rename, delete or edit test
    - Click on`Edit Test`
    - Select the type of questions (*Output, MCQ or Code*)
    - Type the Question on the `Description` field
    - For "Output" and "MCQ" questions, use the code editor on the right to provide the code you would like the students to see
    - For "Code" questions, leave this field blank for students to fill out
    - Enter the `Solution` (for "Output" and "MCQ" questions)
    - Enter the `Allocated mark` for the question
    - Click `Save` (or `Clear` to restart the question)
    - Once finished, click `Return ->`
    - If you would like for your students to be able to sit a test, click on the course name in the sidenav, find the test and click the `Live` toggle button (which will by default show `Not Live`)
    
  - *_Add Students to Course_*:
      - Once on the Course View, Click `Manage students`
      - Enter the email of the student you wish to add
      - Note: at the current stage of development, only students who have already registered to UniCode can be added to a course

  - *_Remove Students from Course_*:
      - Once on the Course View, Click `Manage students`
      - Look for the student email and click "x"
      
  - *_Marking Test_*:
      - Click on the test you want to mark within the course
      - If the test has student submissions, you will now see some test statistics, including the mark of the automatic marked questions
      - In the "Mark Tests" section toward the bottom. you will see all the students who have submitted the test
      - Students whose test still requires marking display a red `Mark Test` button, click this to mark the test
      - Again, questions that require manual marking ("Code" questions) will display in red
      - Optionally, view the other questions as well, that have been automatically marked. Feel free to adjust the automatically assigned marks
      - When finished, click on `Submit and give feedback ->` to submit the result and optionally provide the student some feedback
      
</details>

### For Students Profile:
<details>
  <summary markdown="span">Instructions for students, click me to expand</summary>

  
  - *_Registration_*: 
    - At the bottom of the Login form on the Home page, click `Sign up`
    - Fill out the registration form with your student email
    - Click `Register`
    
  - *_Login_*: 
    - Fill out Login form using email and password
    - Click `Login`

  - *_Taking Test_*: 
    - Click on Course
    - Select the test to take
    - Fill out the answer for each question
    - Once you are happy with your answers, click the red `Submit test` and confirm
    
  - *_View Results_*: 
    - Click on a test you have submitted (which will display a red 'Submitted' banner)
    - View your result, some summary statistics for the test, and the teacher's feedback (if any)

</details>

___


# Local build instructions

<details>
  <summary markdown="span">Instructions for local build (click me to expand) </summary>

1. Clone this repo and open in terminal
```
$ cd unicode
```

2. Create virtual enviroment and activate venv:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install requirements:

```shell
$ pip install -r requirements.txt
```

4. Deactivate/reactivate venv  
Band-aid fix for now, for strange SQLAlchemy install bug

```shell
$ deactivate
$ source venv/bin/activate
```

5. Change to the app development directory:

```shell
$ cd app-dev
```

6. Launch Flask server:

```shell
$ flask run
```

</details>
