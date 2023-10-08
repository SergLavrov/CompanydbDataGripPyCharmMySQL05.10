
CREATE DATABASE companydb;

CREATE TABLE CompanyInfo (
    name varchar(20),
    address varchar(20),
    phone varchar(20),
    email varchar(20)
);

CREATE TABLE Department (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    manager varchar(20),
    phone varchar(20) UNIQUE,
    email varchar(20) UNIQUE
);

CREATE TABLE Employee (
    id int PRIMARY KEY AUTO_INCREMENT,
    solary float,
    position varchar(20),
    departmentId int,
        FOREIGN KEY (departmentId) REFERENCES Department(id)
);

CREATE TABLE EmployeeProfile (
    id int PRIMARY KEY AUTO_INCREMENT,
    firstname varchar(20),
    surname varchar(20),
    address varchar(20),
    birthDate DATE,
    employeeId int UNIQUE,
        FOREIGN KEY (employeeId) REFERENCES Employee(id)
);

CREATE TABLE EmployeeContact (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(20),
    value varchar(20),
    employeeProfileId int,
        FOREIGN KEY (employeeProfileId) REFERENCES EmployeeProfile(id)
);

INSERT INTO employee (solary, position)
VALUES
    (1000, 'manager'),
    (2000, 'developer'),
    (500, 'salesman');

INSERT INTO EmployeeProfile (firstName, surname, address, birthDate, employeeId)
VALUES
    ('John', 'Smith', 'Europe', '1975-01-01', 1),
    ('Jane', 'King', 'UAR', '1987-01-01', 2),
    ('Tim', 'Divanov', 'Belarus', '1974-10-11', 3)

INSERT INTO EmployeeContact (name, value, EmployeeProfileId)
VALUES
    ('telegram', '@jonsmith', 1),
    ('email', '@jons@qmail.ru', 1),
    ('telegram', '@jane', 2),
    ('email', '@janr@mail.ru', 2),
    ('telegram', '@timan', 3),
    ('email', 'tim@qmail.ru', 3);

CREATE index employeePositionIndex on employee (position);

CREATE VIEW employeeLiteInfo as
SELECT ep.firstName as firstName, ep.surName as surName,
       e.position as position, ep.address as address
FROM employee e
left join EmployeeProfile EP on e.id = EP.employeeId;


CREATE VIEW employeecontactinfo as
SELECT e.position as position, ep.firstName as firstName,
       ep.surName as surName, ec.name as contactType,
       ec.value as contactValue
FROM employee e
left join EmployeeProfile ep on e.id = ep.employeeId
left join EmployeeContact ec on ep.id = ec.employeeProfileId
order by e.position;


import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1005Lavr__",
    database="companydb"
)

cursor = connect.cursor()

print('Result first query:')
try:
    cursor.execute('SELECT * FROM employeeliteinfo')
    result = cursor.fetchall()
    for data in result:
        print(data)

except mysql.connector.Error as error:
    print(f'Failed to read data from table {error}')


    print()
    print('Result second query:')

try:
    cursor.execute('SELECT * FROM employeecontactinfo')
    result = cursor.fetchall()
    for data in result:
        print(data)

except mysql.connector.Error as error:
    print(f'Failed to read data from table {error}')

connect.close()

#.env



