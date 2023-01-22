from pysql import mysqls as ms
import datetime
#####################################################################################################
## การจะใช้คำสั่งใน mysqls ได้ต้องสร้าง database ให้เหมือนในโปรเจคนี้ก่อน ตั้งชื่อ database ว่า foodservice และมี   ##
## table เหมือนใน file net-group16\code\pysql\create_table_and_table_struct\createTable.py         ##
####################################################################################################

print(ms.MySql().getAllUser())


sql = ms.MySql()
# print('--------------------------------------------------')
# ms.MySql().addFoods("somtum", 50)
# ms.MySql().addFoods("pingkai", 60)
# ms.MySql().addFoods("kao", 20)
# ms.MySql().addFoods("ping moo", 90)
print('--------------------------------------------------')
print(sql.getAllFood())
print(type(sql.getFoods('somtum')[0]))
# ms.MySql().deleteFoods('057901', 'kao')

date = datetime.datetime.now()
print(date.strftime("%Y-%m-%d"))

print("--------------------getbillUserDetail-----------------------")
strs = ms.MySql().getbillUserDetail(userId="07055401949")
print(strs)
str1 = ms.MySql().getbillUserDetail("user2")
print(str1)
print("--------------------showAllBill-----------------------")
print(ms.MySql().getAllBill())

#############################################
##          genbillเมื่อลูกค้าสั่ง oder          ##
#############################################
# user2 = ms.MySql()
# user2.genBill('020855', '07055401949', 10)

# user2.genBill('037946', '07055401949', 15)
# user3 = ms.MySql()
# user3.genBill('099793', '02582970396', 100)

print("--------------------Top sell-----------------------")
print(ms.MySql().topsell())
ms.MySql().getbillUserDetail(userId="07055401949")
print("-------------------------------------------")

###################################################


def startClient():
    print('='*15 + '  Welcome to Foodservice  ' + '='*15+'\n')


def checkChoice(choice):
    print("\t1. Login\n\t2. Register\n\t3. Bill history")
    choice = int("Select : ")
    if choice == '1':
        print('Welcome You are going to login')
        loginCmd()
#         send(choice)
    elif choice == '2':
        print('Welcome You are going to register')
        registerCmd()
    elif choice == '3':
        print('This is a Bill history')
        print(ms.MySql().getAllBill())
 
    else:
        print('\t\t' + '!'*5 + ' Invalid option please try again ' + '!'*5 + '\n')


def loginCmd():
    username = input('Username : ')
    password = input('Password : ')
    ms.Mysql.login(username,password)


def registerCmd():
    username = input('Username : ')
    password = input('Password : ')
    address = input('Address : ')
    ms.Mysql.createUser(username, password, address)


print(sql.getbillUserDetail('user3'),"sdfsdf")
strs = ms.MySql().getbillUserDetail("user3")
print(strs)