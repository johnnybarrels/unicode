<p align="center">
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/logos/logo.png?token=ANBLRDVBHRIKZUAMVJAVQTS62H4KI"  width="300" height="200" title="FVCproductions" alt="Unicode_logo">
</p>

---

> # **CITS3403/CITS5504 - Agile Web Development — Final Project**

> ## **Development Team:**

| **Johnny Barrett** | **Ivy Bui** | **Jesse Carter** | **Cesar Gonzalez** |
| :---: |:---:| :---:|:---:|
| [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)    | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)  |[![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)  |

--- 

## Table of Contents

- [Motivation](#motivation)
- [Description](#description)
- [Design Process](#design-process) 
- [How it works](#how-it-works)
- [How to Install from localhost](#how-to-install-from-localhost)
- [License](#license)

---

## **Motivation**

One of the biggest challenges faced by Computer Science and Data Science student is the ability to demostrate our coding skills by completing coding test using pen and paper, at the same time, not able to practice on a real life coding platform that provides a more realistic experience when preparing for exams and to improve our coding skills. 

For this reason we decided to develop **Unicode**, so that professors as well as student can improve the learning experience when it comes to learn how to code.


## **Description**

**Unicode** is an online quiz platform for educational institutions that allows admin/teachers users to create and evaluate coding related tests and users/students to take tests and see results. It is design to provide a friendly experience for studens and teachers without compromising the level of complexity required for developing our coding learning experience.

**Unicode** provides the ability to not only test our theorical knowledge of but also our technical abilities. Teachers/admin have the ability to decide to use from three different questions assestement types: 

- **_Output_**: Based on a code function provided by the teacher, the student should answer the expected output (automated marking)
- **_MCQ_**: Based on a writen question or provided code, the student must select the best answer out of 4 posible options(automated marking)
- **_Write a code_**: Based on the instruction and descriptions provided by the teacherk the student can type down the corresping line of code to achieve the results requested( manual marking)

Another important functionality of **Unicode** is the ability of the admin to organize create tests by course and assign students to different courses. Also, the admin can decide when to enble test to be live(ready to take) for all students enroll in the course.

--- 

## **Design Process**

We decided to use MVC(model view controller) Arquitecture for our project. The *model* refers to an object referencing an entity in a database, the *view* is how that object is presented to the user and the *controller* is a linking class that builds the model from the database, prepares the view based on the model, and the updates and saves the models back to the database.

> - **_User Stories:_**

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
| 10 | `Admin` | I want to be able to display the solutios to my students after the test | 6 |
| 11 | `Admin` | I want to be able to allocate marks to each  question | 3 |
| 12 | `Student` | I want to be able to take the test assigned to me | 7 |
| 13 | `Student` | I want to be able to see my marks, and how they compare to the rest of the class | 8 |
| 14 | `Student` | I want to see the solutions the tests (after) | 9 |


> - **_Model Views:_**

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


> - **_Wireframes_**
<p>
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Wireframes.png?token=ANBLRDWVNLZ7QNXSDACNYKC62JKDA"  width="1000" height="300" title="FVCproductions" alt="color">
</p>



> - **_Color pallets_**
<p>
  <img src="https://raw.githubusercontent.com/johnnybarrels/agile-proj2/master/design/Color_Palette.png?token=ANBLRDSBFD5S4ITZ3B7XB3262JGD2"  width="500" height="400" title="FVCproductions" alt="color">
</p>

---

## **How it Works**

> ### For Admin(Teachers) Profile

- **Teacher**
    - Login using email address and password
    - *_Create a new course_*: 
      - Click on `CREATE A NEW COURSE`
      - Type Course Name
      - Type Course Code
      
    - *_Create a new Test_*: 
      - Click on `CREATE A NEW TEST`
      - Type Test name 
      _
      
    
    - Login using email address and password

---

## **How to Install from localhost**

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 ©
