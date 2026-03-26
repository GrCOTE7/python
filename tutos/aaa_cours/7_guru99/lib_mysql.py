import mysql.connector
# pip install mysql-connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="")

print(db_connection)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
# db_cursor.execute("CREATE DATABASE my_first_db")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
# print all databases
for db in db_cursor:
    print(db)

db_cursor = db_connection.cursor()
db_cursor.execute("USE my_first_db")

db_cursor = db_connection.cursor()
# Here creating database table as student'
# db_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

#Here creating database table as employee with primary key
# db_cursor.execute("CREATE TABLE employee(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")
#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

student_sql_query = "INSERT INTO student(id,name) VALUES(01, 'John')"
employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"
#Execute cursor and pass query as well as student data
db_cursor.execute(student_sql_query)
#Execute cursor and pass query of employee and data of employee
db_cursor.execute(employee_sql_query)
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")
