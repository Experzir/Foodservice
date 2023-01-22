import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
# )
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="foodservice"
        )
mycursor = mydb.cursor()

# my_str = "CREATE DATABASE foodservice"
# my_str = """ALTER TABLE user  
# ADD status VARCHAR(10);"""
# mycursor.execute(my_str)




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


# str = """  CREATE TABLE Food(
#     FID CHAR(6),
#     fname VARCHAR(40),
#     fprice int(5),
#     CONSTRAINT Food_PK PRIMARY KEY (FID)
#   );
#   """
# str = """  CREATE TABLE Bill(
#     BID CHAR(6),
#     UID CHAR(11),
#     FID CHAR(6),
#     total int(5),
#     time date,
#     CONSTRAINT Bill_PK PRIMARY KEY (BID,UID,FID),
#     CONSTRAINT Bill_user_FK FOREIGN KEY(UID)
#         REFERENCES User(UID),
#     CONSTRAINT Bill_food_FK FOREIGN KEY(FID)
#         REFERENCES Food(FID));
#   """
# mycursor.execute(str)