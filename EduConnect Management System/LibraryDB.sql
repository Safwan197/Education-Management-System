create database LibraryDB;
Use LibraryDB;
CREATE TABLE students (
student_id INT IDENTITY(1,1) PRIMARY KEY,
full_name VARCHAR(100),
roll_no VARCHAR(20) UNIQUE,
password VARCHAR(50)
);
CREATE TABLE courses (
course_id INT IDENTITY(1,1) PRIMARY KEY,
course_name VARCHAR(100),
course_code VARCHAR(20)
);
CREATE TABLE student_courses (
id INT IDENTITY(1,1) PRIMARY KEY,
student_id INT FOREIGN KEY REFERENCES students(student_id),
course_id INT FOREIGN KEY REFERENCES courses(course_id)
);
CREATE TABLE books (
book_id INT IDENTITY(1,1) PRIMARY KEY,
title VARCHAR(100),
author VARCHAR(100),
quantity INT
);
CREATE TABLE issued_books (
issue_id INT IDENTITY(1,1) PRIMARY KEY,
student_id INT FOREIGN KEY REFERENCES students(student_id),
book_id INT FOREIGN KEY REFERENCES books(book_id),
issue_date DATETIME,
return_date DATETIME NULL
);
CREATE TABLE marks (
mark_id INT IDENTITY(1,1) PRIMARY KEY,
student_id INT FOREIGN KEY REFERENCES students(student_id),
course_id INT FOREIGN KEY REFERENCES courses(course_id),
marks_obtained INT
);

USE LibraryDB;

CREATE TABLE fees (
    fee_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT NOT NULL FOREIGN KEY REFERENCES students(student_id),
    total_fee FLOAT NOT NULL,
    paid_amount FLOAT DEFAULT 0,
    due_amount FLOAT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'Unpaid',
    payment_date DATE NULL
);

CREATE TABLE admin (
    username VARCHAR(100),
    password VARCHAR(55) 
);
select * from books;

ALTER TABLE students
ADD email VARCHAR(100);
