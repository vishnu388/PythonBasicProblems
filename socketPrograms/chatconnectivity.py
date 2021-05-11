import mysql.connector as connector
from decouple import config

class chatconnectivity:
    def __init__(self):
        self.con = connector.connect(host=config('host'), user=config('user'), password=config('password'), database=config('database'))
        query = 'create table if not exists client1_client2data(clientId int primary key, clientName varchar(150),message varchar(50))'
        cursor = self.con.cursor()#cursor() method create a cursor object
        cursor.execute(query)#Execute SQL Query to create a table into your database
        print("Created..")

    # insert
    def insert(self, clientId, clientName, message):
        query = "insert into client1_client2data(clientId,clientName,message) values ({},'{}','{}')".format(clientId,
                                                                                                    clientName, message)

        print(query)
        cursor = self.con.cursor()  # cursor() method create a cursor object
        cursor.execute(query)  # Execute SQL Query to create a table into your database
        self.con.commit()  # Commit is used for your changes in the database
        print("Data inserted on DB Successfully...")


if __name__ == '__main__':
    operations = chatconnectivity()
    #operations.insert(1, "Vishnu", "Hiii")
    operations.insert(2, "Vardhan", "How r u")