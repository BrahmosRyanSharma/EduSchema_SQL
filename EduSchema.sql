CREATE DATABASE EDUSCHEMA;
USE EDUSCHEMA;
CREATE TABLE Student (
    SID INT AUTO_INCREMENT PRIMARY KEY,
    SName VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE,
    Major VARCHAR(100)
);
INSERT INTO Student (SName, Email, EnrollmentDate, Major)
VALUES ('Brahmos', 'brahmos@gmail.com', '2024-01-01', 'CSE');
INSERT INTO Student (SName, Email, EnrollmentDate, Major)
VALUES ('Charan', 'charan@gmail.com', '2023-01-01', 'CSE');
INSERT INTO Student (SName, Email, EnrollmentDate, Major)
VALUES ('Ashrith', 'ashrith@gmail.com', '2024-01-01', 'CSE');

CREATE TABLE Instructor (
    IID INT AUTO_INCREMENT PRIMARY KEY,
    IName VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    HireDate DATE,
    Department VARCHAR(100)
);

INSERT INTO Instructor (IName, Email, HireDate, Department)
VALUES ('Jimmy', 'jimmy@gmail.com', '2023-02-02', 'Python');
INSERT INTO Instructor (IName, Email, HireDate, Department)
VALUES ('Greg', 'greg@gmail.com', '2022-02-02', 'Java');
INSERT INTO Instructor (IName, Email, HireDate, Department)
VALUES ('Deepak', 'deepak@gmail.com', '2024-02-02', 'DSA');

CREATE TABLE Course (
    CID INT AUTO_INCREMENT PRIMARY KEY,
    CName VARCHAR(100),
    CType VARCHAR(50),
    Credits INT,
    IID INT,
    FOREIGN KEY (IID) REFERENCES Instructor(IID)
);

INSERT INTO Course (CName, CType, Credits, IID)
VALUES ('Python', 'Part Time', 3, 1);
INSERT INTO Course (CName, CType, Credits, IID)
VALUES ('Java', 'Part Time', 4, 2);
INSERT INTO Course (CName, CType, Credits, IID)
VALUES ('DSA', 'Full Time', 10, 3);

CREATE TABLE Assignment (
    AID INT AUTO_INCREMENT PRIMARY KEY,
    CID INT,
    AName VARCHAR(100),
    MaxMarks INT,
    FOREIGN KEY (CID) REFERENCES Course(CID)
);

INSERT INTO Assignment (CID, AName, MaxMarks) VALUES (1, 'Python 1', 10);
INSERT INTO Assignment (CID, AName, MaxMarks) VALUES (2, 'Java 2', 10);
INSERT INTO Assignment (CID, AName, MaxMarks) VALUES (3, 'DSA 3', 20);

CREATE TABLE Student_Course (
    SID INT,
    CID INT,
    EnrollmentDate DATE,
    PRIMARY KEY (SID, CID),
    FOREIGN KEY (SID) REFERENCES Student(SID),
    FOREIGN KEY (CID) REFERENCES Course(CID)
);

INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (1, 1, '2024-01-01');  -- Brahmos enrolls in Python

INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (2, 2, '2023-01-01');  -- Charan enrolls in Java

INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (3, 3, '2024-01-01');  -- Ashrith enrolls in DSA

-- Additional enrollments
INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (1, 2, '2024-01-01');  -- Brahmos also enrolls in Java

INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (2, 3, '2023-01-01');  -- Charan also enrolls in DSA

INSERT INTO Student_Course (SID, CID, EnrollmentDate)
VALUES (3, 1, '2024-01-01');  -- Ashrith also enrolls in Python

CREATE TABLE Grades (
    SID INT,
    AID INT,
    MarksObtained INT,
    Grade CHAR(2),
    PRIMARY KEY (SID, AID),
    FOREIGN KEY (SID) REFERENCES Student(SID),
    FOREIGN KEY (AID) REFERENCES Assignment(AID)
);

-- Grades for Brahmos (SID = 1)
INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (1, 1, 8, 'B+');  -- Brahmos' grade for Python 1 assignment

INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (1, 2, 9, 'A');  -- Brahmos' grade for Java 1 assignment

-- Grades for Charan (SID = 2)
INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (2, 2, 7, 'B');  -- Charan's grade for Java 1 assignment

INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (2, 4, 9, 'A');  -- Charan's grade for DSA 1 assignment

-- Grades for Ashrith (SID = 3)
INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (3, 4, 15, 'A');  -- Ashrith's grade for DSA 1 assignment

INSERT INTO Grades (SID, AID, MarksObtained, Grade)
VALUES (3, 1, 7, 'B');  -- Ashrith's grade for Python 1 assignment

CREATE TABLE DeletedCourses (
    CID INT PRIMARY KEY,
    CName VARCHAR(255),
    CType VARCHAR(50),
    Credits INT,
    IID INT,
    DeletedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM Grades;
SELECT * FROM Courses;
SELECT * FROM Student;
SELECT * FROM Instructor;
SELECT * FROM Assignment;
SELECT * FROM Student_Course;