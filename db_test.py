# project (python with sql data base)
import sqlite3
db = sqlite3.connect("DB.sqlite")
# create a table here
try:
    db.execute("""create table student( Roll text, Name text, Math text, Science text, Computer text)""")
except:
    pass


def addStudent():
    list1 = ["Roll","Name","Math","Science","Computer"]
    list2 = []
    for item in list1:
        list2.append(input("Enter %s:"%item))
    db.execute("insert into student values(?,?,?,?,?)",list2)
    db.commit()
    print("-----------Data stored---------")


def calculatePercentage():
    roll = input("Enter roll number to calculate the percentage:")  # 5
    cursor = db.cursor()
    cursor.execute("select * from student where Roll = ?", [roll])
    print(cursor.fetchall())
    cursor.close()

def showData():
    cursor = db.cursor()
    cursor.execute("select * from student")
    print(cursor.fetchall())
    cursor.close()


while True:
    ch = int(input("1.Addstudent\n2. Calculate percentage\n3.Show all data\nEnter choice:"))
    if ch == 1:
        addStudent()
    elif ch == 2:
        calculatePercentage()
    elif ch == 3:
        showData()
