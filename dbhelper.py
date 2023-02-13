from sqlite3 import Cursor
import mysql.connector as connector

class DB:
    def __init__(self):
        self.con=connector.connect(
        host="",
        port="",
        user='',
        password='',
        database='')
        query='create table if not exists user(userId int PRIMARY KEY,userName varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    #Insert
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone)values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User Saved to Database")
    #Fetch All
    def fetch_all(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ",row[0])
            print("User Name : ",row[1])
            print("Phone No : ",row[2])
    #Delete
    def delete_user(self,userId):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        record = [item[0]for item in cur.fetchall()]
        if userId not in record:
            print("ID Not Found")
        else:
            query='delete from user where userId = {}'.format(userId)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Deleted")
        
    #update
    def update_user(self,userId,newname,newphone):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        record = [item[0]for item in cur.fetchall()]
        uid = int(input("Enter Id To Update"))
        if uid not in record:
            print("id Not Found")
        else:
            query="update user set userName= '{}' , phone = '{}' where userId={}".format(newname,newphone,uid)
            cur=self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print('updated')
