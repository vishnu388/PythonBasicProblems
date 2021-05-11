"""
Author: vishnu
Date: 04/05/2021
Title: Perform CRUD Operations
"""
from decouple import config
import mysql.connector as connector
import logging
from database import logger
logger.setLevel(logging.INFO)

"""
in this operation we connect pycharm to mysql database
here we are passing variables operation like insert, update and Delete operations
"""

class CRUD:
    def __init__(self):
        self.con = connector.connect(host=config('host'), user=config('user'), password=config('password'), database=config('database'))
        query = 'create table if not exists studentdata(studentId int primary key, studentName varchar(150),phone varchar(50))'
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        print("Created..")

    # insert
    def insert(self, studentId, studentName, phone):
        query = "insert into studentdata(studentId,studentName,phone) values ({},'{}','{}')".format(studentId, studentName, phone)
                                                                                                
        print(query)
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        self.con.commit()# Commit is used for your changes in the database
        print("Data inserted on DB Successfully...")

    # Select
    def select(self):
        query = "select *from studentdata"
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        for row in cur:
            print("studentId : ", row[0])
            print("studentName : ", row[1])
            print("Phone : ", row[2])

    # Delete Query
    def delete(self, studentId):
        query = "delete from studentdata where studentId = {}".format(studentId)
        print(query)
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        self.con.commit()# Commit is used for your changes in the database
        print("Deleted Successfully....")

    # Update Query
    def update(self, studentId, newName, newPhone):
        query = "update studentdata set studentName = '{}', phone = '{}' where studentId = {}".format(newName, newPhone,
                                                                                                      studentId)
        print(query)
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        self.con.commit()# Commit is used for your changes in the database
        print("Updated Successfully...")


if __name__ == '__main__':
    operations = CRUD()
    #operations.insert(11, "Vishnu", "8106261925")
    #operations.insert(12, "Kiran", "9989988301")
    #operations.insert(13, "Ashok", "966646639")
    #operations.insert(14, "Jagan", "9666466639")
    #operations.insert(15, "Ajay", "9701560019")
    #operations.select()
    #operations.delete(13)
    #operations.update(14, "Ashok", "9666466639")