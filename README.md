<p align="center">
  <img name="logo" src="design/logos/logo.png"  width="300" height="200" title="FVCproductions" alt="Unicode_logo">
</p>

---

# UniCode

### A proof-of-concept platform application for creating, sitting, and assessing coding exams


One of the biggest challenges faced by Computer Science, Data Science and Software Engineering students is the inability to demostrate our true coding ability during tests and exams, as we exhaustedly try to make sure the indentation on our hand-written linked list class defintion is correct. Instead of plain old pen and paper, why not allow students to be assessed on a more realistic platform, removing the hassle of the scribble, and providing some of the staple creature comforts like syntax highlighting? (and yes, we remembered to turn AutoComplete off)!

For this reason we decided to develop **UniCode**, so that students and professors alike can enjoy the experience of learning and teaching how to code just a little bit more.


## **Description**

**UniCode** is an online test/exam platform for educational institutions that allows administrator users (teachers) to create and evaluate coding related tests, and for users/students to sit these tests and see results. It is designed to provide a friendly experience for studens and teachers without compromising the level of complexity required for developing the coding learning experience.

**UniCode** provides the ability to not only test students' theoretical knowledge but also their technical abilities. Teachers have the ability to select from three different questions assesment types: 

- **_Output_**: Based on an excerpt of code provided by the teacher, the student is required to enter the expected output. (automated marking).
- **_MCQ_**: Based on a written question and/or provided code, the student must select the best answer out of up to 4 possible options. (automated marking)
- **_Code_**: This is where the students get to have the most fun. Based on the question description provided by the teacher, the student can use the code editor to write their class, function or method, or whatever has been asked of them! These questions are flagged for manual marking by the teacher (we hope to have an in-browser code interpreter in the future)!

Another important functionality of **UniCode** is the ability of the teacher to organise all of their tests and students into their respective courses, choosing which tests to display to students and when.


## Two types of users

The platform is built to cater for two types of users: Teachers/Lecturers and Students. Their respective abilities within the platform are:

### Teacher/Lecturer

- Create, edit, delete, update coding tests and exams
- Organise tests and exams into courses
- Add/remove students from courses
- Have tests Live (visible to students) or hidden, with the flick of a switch
- Use a guided test marking dashboard
- Seamlessly provide student feedback

### Student

- Sit tests and exams set by teachers/lecturers
- View marks, and how they compare to other students
- View feedback from teachers
- View test solutions once made available

___

## Local build

<details>
  <summary markdown="span">Instructions for installation in localhost (click me to expand) </summary>

1. Unzip agile-proj2.zip and cd to directory:
```
$ cd agile-proj2
```

2. Create virtual enviroment and activate venv:

```shell
$ python -m venv venv

# To activate:
$ source venv/bin/activate
```
or

```shell
$ python3 -m venv venv

# To activate:
$ source venv/bin/activate
```

3. Install requirements:

```shell
$ pip install -r requirements.txt
```

4. Change to the app development directory:

```shell
$ cd app-dev
```

5. Launch Flask server:

```shell
$ flask run
```

Note: for whatever reason, the required package `python-dotenv` can play up straight after installation. If you receive an ImportError from this package after running `flask run`, do the following:
```shell
$ cd ..
$ deactivate
$ source venv/bin/activate
$ cd app-dev
$ flask run
```
This should resolve the issue!

</details>



## **How to Use**

### For Admin(Teachers) Profile:
<details>
  <summary markdown="span">Instructions for admin, click me to expand</summary>
  
  - *_Login_*: 
    - Fill out Login form using one of the provided administrator accounts:
      - tim@french.com
      - tom@smoker.com
      - haolin@wu.com
    - The password for each of these accounts is simply: password
    - Click `Login`
    
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

Instructions for students, click me to expand
  
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

 
## **What's Next?**

We believe that **UniCode** has immense potential to keep growing to become an even more robust educational tool for students and teachers. As all developers know, development never ends, and as such here's a list of where we're at and what the next steps might be:

  - Increased language support (currently only Python)
  - Allow multiple teachers to administrate the same course
  - Fuzzy matching for 'Output' question submissions, potentially raising a 'needs marking' flag if a provided answer is close to the given solution
  - Allow teachers to save questions to use again later, and potentially share with other teachers!
  - Keeping students up to date with their marks and tests via email
  - Integration with educational institution's database
  - And the big goal for now: _get code running in the browser !!!_

<br>

**UniCode**: Because nobody likes writing code with a pen and pad
  
## Development Team

| **Johnny Barrett** | **Ivy Bui** | **Jesse Carter** | **Cesar Gonzalez** |
| :---: |:---:| :---:|:---:|

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 ©
