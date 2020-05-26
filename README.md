<p align="center">
  <img name="logo" src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/logos/logo.png?token=ANBLRDVBHRIKZUAMVJAVQTS62H4KI"  width="300" height="200" title="FVCproductions" alt="Unicode_logo">
</p>

---

> # **CITS3403/CITS5504 - Agile Web Development - Final Project**
> **Semester 1, 2020**

## **Development Team:**

| **Johnny Barrett** | **Ivy Bui** | **Jesse Carter** | **Cesar Gonzalez** |
| :---: |:---:| :---:|:---:|
| <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Team_photos/johnny.jpeg?token=ANBLRDTCEU53VE7KN3HKCC262UGAW" width="100" height="100" />  | <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Team_photos/Ivy.png?token=ANBLRDTDUJ6NDSLKV2FKWBS62UFZI" width="100" height="100" />| <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Team_photos/jesse_photo.png?token=ANBLRDXVPFXG75QRS4ERLU262UF62" width="100" height="100" />    | <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Team_photos/cesar_photo.png?token=ANBLRDWIKER7RWJBKC7E6DK62UF4E" width="100" height="100" />  |


--- 

## Table of Contents

- [**Development Team:**](#development-team)
- [Table of Contents](#table-of-contents)
- [**Motivation**](#motivation)
- [**Description**](#description)
- [**Design Process**](#design-process)
- [**How to Install from localhost**](#how-to-install-from-localhost)
- [**How to Use**](#how-to-use)
  - [For Admin(Teachers) Profile:](#for-adminteachers-profile)
  - [For Students Profile:](#for-students-profile)
- [How to Test UniCode](#how-to-test-unicode)
  - [**_unittest_**:](#unittest)
  - [**_sytemtest_**:](#sytemtest)
  - [systemtest will test the following:](#systemtest-will-test-the-following)
- [**What's Next?**](#whats-next)
- [License](#license)


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

---

## **Motivation**

One of the biggest challenges faced by Computer Science, Data Science and Software Engineering students is the inability to demostrate our true coding ability during tests and exams, as we exhaustedly try to make sure the indentation on our hand-written linked list class defintion is correct. Instead of plain old pen and paper, why not allow students to be assessed on a more realistic platform, removing the hassle of the scribble, and providing some of the staple creature comforts like syntax highlighting? (and yes, we remembered to turn AutoComplete off)!

For this reason we decided to develop **UniCode**, so that students and professors alike can enjoy the experience of learning and teaching how to code just a little bit more!

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## **Description**

**UniCode** is an online test/exam platform for educational institutions that allows administrator users (teachers) to create and evaluate coding related tests, and for users/students to sit these tests and see results. It is designed to provide a friendly experience for studens and teachers without compromising the level of complexity required for developing the coding learning experience.

**UniCode** provides the ability to not only test students' theoretical knowledge of but also their technical abilities. Teachers have the ability to select from three different questions assesment types: 

- **_Output_**: Based on an excerpt of code provided by the teacher, the student is required to enter the expected output. (automated marking).
- **_MCQ_**: Based on a written question and/or provided code, the student must select the best answer out of up to 4 possible options. (automated marking)
- **_Code_**: This is where the students get to have the most fun. Based on the question description provided by the teacher, the student can use the code editor to write their class, function or method, or whatever has been asked of them! These questions are flagged for manual marking by the teacher (we hope to have an in-browser code interpreter in the future)!

Another important functionality of **UniCode** is the ability of the teacher to organise all of their tests and students into their respective courses, choosing which tests to display to students and when.


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## **Design Process**

Unicode is built using the MVC (model view controller) architecture. The *model* refers to an object referencing an entity in a database, the *view* is how that object is presented to the user, and the *controller* is a linking class that builds the model from the database, prepares the view based on the model, displays it to the user, and takes user input and adjusts the model and database accordingly.

The user stories developed were:

| # | User | User Story | Story Point |
| --- | :---: | --- | :---: |
| 1 | `Admin` | I want to be able to create coding tests | 1 |
| 2 | `Admin` | I want to be able to group my tests into courses | 1 |
| 3 | `Admin` | I want to be able to edit, delete, rename and make live tests | 2 |
| 4 | `Admin` | I want to be able to control student access to the tests | 3 |
| 5 | `Admin` | I want to have a mix of questions available to me | 1 |
| 6 | `Admin` | I want to have an in-built code editor | 1 |
| 7 | `Admin` | I want to active and deactive tests | 10 |
| 8 | `Admin` | I want to be able to manually mark tests | 4 |
| 9 | `Admin` | I want to see my student's results of my tests/courses | 5 |
| 10 | `Admin` | I want to be able to display the solutions to my students after the test | 6 |
| 11 | `Admin` | I want to be able to allocate marks to each  question | 3 |
| 12 | `Student` | I want to be able to take the test assigned to me | 7 |
| 13 | `Student` | I want to be able to see my marks, and how they compare to the rest of the class | 8 |
| 14 | `Student` | I want to see the solutions the tests (after) | 9 |


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

And so the corresponding views were:
| User | View |
| :---: | :--- | 
| `All` | Login | 
| `All` | Registration |
| `Admin` | Course View | 
| `Admin` | Create a new course prompt | 
| `Admin` | Single course view (contains each test) | 
| `Admin` | Create new test prompt | 
| `Admin` | Test result dashboard | 
| `Admin` | New test,add questions (3 types options, Description answers and allocated marks | 
| `Admin` | Test preview (what it looks to students) | 
| `Student` | Single course view (contain each available test) | 
| `Student` | Taking test view | 
| `Student` | Test result view |


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>


- **_Wireframes_**
<p>
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Wireframes.png?token=ANBLRDWVNLZ7QNXSDACNYKC62JKDA"  width="1000" height="300" title="FVCproductions" alt="color">
</p>


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>


- **_Color palettes_**
<p>
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Color_Palette.png?token=ANBLRDSBFD5S4ITZ3B7XB3262JGD2"  width="500" height="400" title="FVCproductions" alt="color">
</p>


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

- **_Database_**

<p align="center">
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Unicode%20database.png?token=ANBLRDUQKIWDZXYOVX7N4R262S5MA"  width="800" height="500" title="FVCproductions" alt="color">
</p>

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>


## **How to Install from localhost**

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

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

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
    

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## How to Test UniCode

⚠️ Firstly, ensure you are in the `app-dev` folder:
```shell
$ cd app-dev
```

### **_unittest_**:

Tests:  
  - Password hashing: `test_set_pw` and `test_set_pw2`
  - Main page login: `test_main_page`
  - Registration module `test_users_can_register`
  - Test that only registered users can login `test_users_cannot_unless_registered`
  - Test that there are not duplicate registration `test_duplicate_user_registration_throws_error`  
  
To run these tests, simply run:
  
```shell
$ python -m Tests.unittest
```
in your terminal.

### **_sytemtest_**:

⚠️ Please make sure to run system test last.

To run the systemtests, in `__init__.py`, manually change the Config object to `TestConfing`. This line has been commented for you. This prevents the test from overwriting the existing database.
 
```shell
python -m Tests.system
```

### systemtest will test the following:

  - Login page for students: `test_login_user`
  - Login page for admin: `test_login_admin`
  - New user registration and login: `test_user_registration`


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>
 
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
  

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 ©
