"""
Author: vishnu
Date: 04/05/2021
Title: Perform CRUD Operations
"""

import mysql.connector as connector
import logging
from database import logger
logger.setLevel(logging.INFO)

class CRUD:
    def __init__(self):
        self.con = connector.connect(host='localhost', user='root', password='Vishnu@388', database='pythondb')

        query = 'create table if not exists studentdata(studentId int primary key, studentName varchar(150),phone varchar(50))'

        cur = self.con.cursor()

        cur.execute(query)

        print("Created..")
        # insert

    def insert(self, studentId, studentName, phone):
        query = "insert into studentdata(studentId,studentName,phone) values ({},'{}','{}')".format(studentId, studentName,
                                                                                                phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data inserted on DB Successfully...")

    # Select
    def select(self):
        query = "select *from studentdata"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("studentId : ", row[0])
            print("studentName : ", row[1])
            print("Phone : ", row[2])

    # Delete Query
    def delete(self, studentId):
        query = "delete from studentdata where studentId = {}".format(studentId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted Successfully....")

    # Update Query
    def update(self, studentId, newName, newPhone):
        query = "update studentdata set studentName = '{}', phone = '{}' where studentId = {}".format(newName, newPhone,
                                                                                                      studentId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
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
    operations.update(14, "Ashok", "9666466639")