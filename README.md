<p align="center">
  <img name="logo" src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/logos/logo.png?token=ANBLRDVBHRIKZUAMVJAVQTS62H4KI"  width="300" height="200" title="FVCproductions" alt="Unicode_logo">
</p>

---

> # **CITS3403/CITS5504 - Agile Web Development - Final Project**
> # <p align="center"> **Semester 1, 2020** </p>

## **Development Team:**

| **Johnny Barrett** | **Ivy Bui** | **Jesse Carter** | **Cesar Gonzalez** |
| :---: |:---:| :---:|:---:|
| <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/johnny.jpeg?token=ANBLRDQC3LZ7RND2QTJBAE262S5QI" width="100" height="100" />  | <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Ivy.png?token=ANBLRDQR53OQ4G274BL3HWK62TS4G" width="100" height="100" />| <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/jesse_photo.png?token=ANBLRDWSQTNJKKDOHF3BFE262TTUQ" width="100" height="100" />    | <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/cesar_photo.png?token=ANBLRDQOFBVXJNZAKIHNZC262TTZ6" width="100" height="100" />  |


--- 

## Table of Contents

- [Motivation](#motivation)
- [Description](#description)
- [Design Process](#design-process) 
- [How to Install from localhost](#how-to-install-from-localhost)
- [How to Use](#how-to-use)
- [How to Test](#how-to-test-unicode)
- [Limitations](#limitations)
- [What is Next](#what-is-next)
- [License](#license)


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

---

## **Motivation**

One of the biggest challenges faced by Computer Science and Data Science student is the ability to demostrate our coding skills by completing coding test using pen and paper, at the same time, not able to practice on a real life coding platform that provides a more realistic experience when preparing for exams and to improve our coding skills. 

For this reason we decided to develop **Unicode**, so that professors as well as student can improve the learning experience when it comes to learn how to code.

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## **Description**

**Unicode** is an online quiz platform for educational institutions that allows admin/teachers users to create and evaluate coding related tests and users/students to take tests and see results. It is design to provide a friendly experience for studens and teachers without compromising the level of complexity required for developing our coding learning experience.

**Unicode** provides the ability to not only test our theorical knowledge of but also our technical abilities. Teachers/admin have the ability to select from three different questions assesment types: 

- **_Output_**: Based on a code function provided by the teacher, the student should answer the expected output (automated marking)
- **_MCQ_**: Based on a writen question or provided code, the student must select the best answer out of 4 posible options(automated marking)
- **_Write a code_**: Based on the instruction and descriptions provided by the teacherk the student can type down the corresping line of code to achieve the results requested( manual marking)

Another important functionality of **Unicode** is the ability of the admin to organize create tests by course and assign students to different courses. Also, the admin can decide when to enble test to be live(ready to take) for all students enroll in the course.


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## **Design Process**

We decided to use MVC(model view controller) Arquitecture for our project. The *model* refers to an object referencing an entity in a database, the *view* is how that object is presented to the user and the *controller* is a linking class that builds the model from the database, prepares the view based on the model, and the updates and saves the models back to the database.

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


- **_Color pallets_**
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
  <summary markdown="span">Instructions for installation in localhost, click me to expand</summary>

1. Clone repository using `https://github.com/johnnybarrels/agile-proj2.git`

```shell
$ git clone https://github.com/johnnybarrels/agile-proj2.git
```

2. Change working directory to agile-proj2:
```
$ cd agile-proj2
```

3. Create virtual enviroment and activate venv:

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

2. Install requirements:

```shell
$ pip install -r requirements.txt
```

3. Make sure you are on the correct working directory for the app:

```shell
$ cd app-dev
```

3. Launch Database: 

```shell
$ flask db init
$ flask db migrate -m ' ' 
$ flask db upgrade
```

4. Populate Database:
  - We have created python function to automtically populate the database (use flask shell to access python on terminal)
  ```shell
  $ flask shell
  ```
  - Import the function and execute
  
  ```python
  from app.db_tools import purge_and_load 
  purge_and_load()
  exit() 
  ```
  
5. launch app:

```shell
$ flask run
```

</details>

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## **How to Use**

### For Admin(Teachers) Profile:
<details>
  <summary markdown="span">Instructions for admin, click me to expand</summary>
  
  - *_Login_*: 
    - Fill up Login form using email and password
    - Click `Login`
    
  - *_Create a New Course_*: 
    - Click on `CREATE A NEW COURSE` or "+" icon next to Course
    - Type Course Name
    - Type Course Code
    - Click `Create Course`
     
  - *_Create a New Test_*: 
    - Select the Course on the right panel
    - Click on `New Test`
    - Type Test name
    - Click `Create Test`
    - Click on the new created test
      - (Optional) Click on dropdown to rename, delete or edit test
    - Click on`Edit Test`
    - Click on `Add +` to add a new question
    - Select the type of questions (*Output, MCQ or Write a code*)
    - Type the Question on the `Description` field
    - Type `Solution`
    - Type the `Allocated mark` for the question
    - Click `Save` (or `Clear` to restart the questions)
    - Once finshes, click `Save and return`
    - Once finishing creating the questions, click the course name on the righ panel
    - Click `Not Live` to make sure test live
    
  - *_Add Students to Course_*:
      - Once on the Course View, Click `Manage students`
      - Type the Student number

  - *_Delete Students from Course_*:
      - Once on the Course View, Click `Manage students`
      - Look for the student email and click "x"
      
  - *_Marking Test_*:
      - Pending
      
  - *_Publish Test Results_*:
      - Pending
      
</details>

### For Students Profile:

<details>
  <summary markdown="span">Instructions for students, click me to expand</summary>
  
  - *_Registration_* (for new users only): 
    - Click on `Sign up`
    - Fill up registration form 
    - Click `Register`
    
  - *_Login_*: 
    - Fill up Login form using email and password
    - Click `Login`

  - *_Taking Test_*: 
    - Click on Course
    - Select the test to take
    - Once test completed Select `Submit test`
    
  - *_View Results_*: 
    - Pending
    
</details>

<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>

## How to Test Unicode

First make sure you are in the `app-dev`.

### **_unittest_**:

For testing password hashing and test creation.

  - To use just type on the terminal the following command:
  
```shell
python -m Tests.unittest
```


### **_sytemtest_**:

⚠️ Please make sure to run system test last and to manually change the Config object to `TestConfing` in the `__init__.py` overwrite existing to avoid ovewriting existing database.

Using selenium to test our app with firefox web browser
 - Test for student login
 - Test for admin login
 - Test for student registration and login
 
```shell
python -m Tests.system
```


<a name="bottom" href="https://github.com/johnnybarrels/agile-proj2#logo"><img align="right" border="0" src="https://raw.githubusercontent.com/CCOSTAN/Home-AssistantConfig/master/config/www/custom_ui/floorplan/images/branding/up_arrow.png" width="22" ></a>
 
## **Limitations**
 
## **What is Next**


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 ©
