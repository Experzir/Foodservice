import mysql.connector
import random
import datetime
from pysql import mysqls

# เตือนการใช้ object เดียวในการ aad ค่าในตารางจะทำให้ id มันซ้ำกัน แต่จะใช้ในการ genbill ได้
class MySql:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="foodservice"  # ชื่อ database ที่ต้องการ connect ##############
        )
        self.uid = str({0: 11}).format(
            random.randint(1, 9999999999)).replace(" ", "0")
        self.fid = str({0: 6}).format(
            random.randint(1, 999999)).replace(" ", "0")
        self.bid = str({0: 6}).format(
            random.randint(1, 999999)).replace(" ", "0")

    def createUser(self, username, password, address):
        mycursor = self.__mydb.cursor()
        uid = self.uid
        my_str = "INSERT INTO User VALUES('"+self.uid + \
            "','"+username+"','"+password+"','"+address+"');"
        # chek user
        b = bool(self.getUser(username=username))
        if(not b):
            mycursor.execute(my_str)
            self.__mydb.commit()
            print("UserID: {} name: {} created.".format(self.uid, username))
            return (True,self.uid)
        elif(b):
            print("User name: {} has been used.".format(username))
            return False

    def getAllUser(self):
        mycursor = self.__mydb.cursor()
        my_str = """select * from user;"""
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        stemp = ""
        for x in myresult:
            stemp = stemp+"UID: {} UName: {} Password: {} Address: {}\n".format(
                x[0], x[1], x[2], x[3])
        return stemp

    def showUser(self, UIDs="", username=""):
        mycursor = self.__mydb.cursor()
        my_str = ""
        uid = "select * from user where uid = '{}';".format(UIDs)
        name = "select * from user where UName = '{}';".format(username)
        seall = "select * from user where uid = '{}' and UName = '{}';".format(
            UIDs, username)
        if UIDs == "":
            my_str = name
        elif username == "":
            my_str = uid
        else:
            my_str = seall
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        if(not myresult):
            print("NO data found.")
        for x in myresult:
            print("UID: {} UName: {} Password: {} Address: {}".format(
                x[0], x[1], x[2], x[3]))

    def getUser(self, UIDs="", username=""):
        mycursor = self.__mydb.cursor()
        my_str = ""
        uid = "select * from user where uid = '{}';".format(UIDs)
        name = "select * from user where UName = '{}';".format(username)
        seall = "select * from user where uid = '{}' and UName = '{}';".format(
            UIDs, username)
        if UIDs == "":
            my_str = name
        elif username == "":
            my_str = uid
        else:
            my_str = seall
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        return myresult  # returntype ->> list<tuple>

    def dropUser(self, UIDs, username):
        mycursor = self.__mydb.cursor()
        my_str = "DELETE FROM user WHERE uid = '{}' and UName = '{}'".format(
            UIDs, username)
        mycursor.execute(my_str)
        print('User: {} droped.'.format(username))
        self.__mydb.commit()
        return True

    # Food
    def addFoods(self, name, price):
        mycursor = self.__mydb.cursor()
        fid = self.fid
        my_str = "INSERT INTO food VALUES('{}','{}',{});".format(
            fid, name, price)
        # chek user
        b = bool(self.getFoods(fname=name))
        if(not b):
            # print(my_str)
            mycursor.execute(my_str)
            self.__mydb.commit()
            print("ID: {} Food: {} Price: {} was added.".format(fid, name, price))
            return True
        elif(b):
            print("There is a food with this name '{}'".format(name))

    def deleteFoods(self, fid, fname):
        mycursor = self.__mydb.cursor()
        my_str = "DELETE FROM food WHERE fid = '{}' and fname = '{}'".format(
            fid, fname)
        mycursor.execute(my_str)
        print('Food: {} droped.'.format(fname))
        self.__mydb.commit()
        return True

    def getAllFood(self):
        mycursor = self.__mydb.cursor()
        my_str = """select * from food;"""
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        stemp = ""
        for x in myresult:
            stemp = stemp + "FID: {} Food name: {} price: {}\n".format(
                x[0], x[1], x[2])
        return stemp

    def getFoods(self, fname):
        mycursor = self.__mydb.cursor()
        my_str = "select * from food where fname = '{}';".format(fname)
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        return myresult,True  # returntype ->> list<tuple>
    def getFoodbyID(self, fid):
        mycursor = self.__mydb.cursor()
        my_str = "select * from food where fid = '{}';".format(fid)
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        return myresult[0]
    # pirvate function
    def genBill(self, fid, uid, total):
        mycursor = self.__mydb.cursor()
        bid = self.bid
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        my_str = "INSERT INTO Bill VALUES('{}','{}','{}',{},'{}');".format(
            bid, uid, fid, total, date)
        mycursor.execute(my_str)
        self.__mydb.commit()
    # def order(self,fid,uid,total):
    #     for i in a:
    #       print()
    #     print()

    def getAllBill(self):
        mycursor = self.__mydb.cursor()
        my_str = "select * from Bill"
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        stemp = ""
        for e in myresult:
            s = "bid: {}, uid: {}, fid: {}, total: {}, date: {}\n".format(
                e[0], e[1], e[2], e[3], e[4].strftime("%d-%m-%Y"))
            stemp = stemp+s
        return stemp

    def getbillUserDetail(self, username="", userId=""):
        mycursor = self.__mydb.cursor()
        get = ""
        result = ""
        if username == "":
            get = 'Bill.uid'
            result = userId
        elif userId == "":
            get = 'User.uname'
            result = username
        elif not(username == "") and not(userId == ""):
            get = 'User.uname'
            result = username
        else:
            get = 'User.uname'
            result = "---"

        my_str = """
        select Bill.bid,User.uid,User.uname,Bill.time
        from Bill,User
        where Bill.uid = User.uid and {} = '{}'
        GROUP BY bid,uid
        """.format(get, result)

        mycursor.execute(my_str)
        myresult = mycursor.fetchall()

        str_result = ""
        headers = ""
        detail_temp = ""
        for e in myresult:
            headers = """+++++++++++++++++++++++++++++++++++++++++++++++++
            \nBill_ID: {} User: {} Time: {}\n""".format(e[0], e[2], e[3].strftime("%d-%m-%Y"))

            st = """
        select Food.fname,Food.fprice,Bill.Total
        from Bill,Food
        where Bill.fid = Food.fid AND Bill.bid = '{}'
        """.format(e[0])
            mycursor.execute(st)
            result = mycursor.fetchall()
            sumprice = 0
            for i in result:
                detail_temp = detail_temp + \
                    "\t{}  price: {} quantity: {}\n".format(i[0], i[1], i[2])
                sumprice = sumprice + (i[1]*i[2])
            s = "Total: " + \
                str(sumprice) + \
                " Baht\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n"
            str_result = str_result + headers + detail_temp + s
            detail_temp = ""
        return str_result

    def topsell(self):
        mycursor = self.__mydb.cursor()
        my_str = """select Bill.fid,Food.fname,SUM(total) sumTotal
            from Bill,Food
            where Bill.fid = Food.fid
            group by Bill.fid,Food.fname
            ORDER BY sumTotal DESC;;
         """
        mycursor.execute(my_str)
        myresult = mycursor.fetchall()
        stemp = ""
        for e in myresult:
            stemp = stemp+"FID: {},Food name: {}, Total: {}\n".format(e[0],e[1],e[2])
        return stemp
    
    def login(self,username,password):
        if username == "" or password == "":
            print("Username or Password could not empty!\n")
        else:
            mycursor = self.__mydb.cursor()
            mycursor.execute("select * from User where UName=%s and password=%s",(username,password))
            row = mycursor.fetchone()
            if row == None:
                print("Error Invalid Username & Password\n")
                return False
            else:
                print("Welcome You are logged!!\n")
                return True
    
    def loginAd(self,username,password):
        if username == "" or password == "":
            print("Username or Password could not empty!\n")
        else:
            mycursor = self.__mydb.cursor()
            if username == "admin" and password == "admin":
                mycursor.execute("select * from User where UName=%s and password=%s",(username,password))
                row = mycursor.fetchone()
                if row == None:
                    print("Error Invalid Username & Password\n")
                    return False
                else:
                    print("Welcome You are logged!!\n")
                    return True
        
# if __name__ == '__main__':
#     MySql().createUser('user1', 'user1', 'kku')
# if __name__ == '__main__':
#     print('============end============')
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="foodservice"
#     )
#     # str = """ DROP TABLE User  ;"""
#     str = """  CREATE TABLE User(
#     UID CHAR(11),
#     UName VARCHAR(40),
#     password VARCHAR(20),
#     UAddress VARCHAR(80),
#     CONSTRAINT User_PK PRIMARY KEY (UID)
#   );
#   """
#     mycursor = mydb.cursor()
#     mycursor.execute(str)
