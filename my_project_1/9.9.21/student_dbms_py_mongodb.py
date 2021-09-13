import pymongo
from pymongo.collection import Collection

my_client =pymongo.MongoClient('localhost:27017')
my_db=my_client["mydatabase"]

my_col: Collection = my_db["students"]

class Student:
    def __init__(self,options):
        self.name =options["name"]
        self.rollno =options["rollno"]
        self.m1 =options["m1"]
        self.m2 =options["m2"]

    def insert_name(self):
        return self.name

    def insert_rollno(self):
        return self.rollno

    def insert_m1(self):
        return self.m1

    def insert_m2(self):
        return self.m2

print("\nOperations used, ")
print("1.Insert Student details\n2.Search Details of a Student\n3.Update Details of Student\n4.Delete Student Details\n5.Exit")

x=True
while x:
    ch = int(input("Enter choice:"))
    if ch == 1:
        name = input("enter the student name:")
        rollno = input("enter the student rollno:")
        m1 = input("enter the student marks:")
        m2 = input("enter the student marks:")

        student = Student({"name": name, "rollno": rollno, "m1": m1, "m2": m2})

        s = {"name": student.name, "rollno": student.rollno, "m1": student.m1, "m2": student.m2}
        my_col.insert_one(s)

    if ch == 2:
        name=input("enter the name:")
        for record in my_col.find({"name":name}):
            print(record)

    if ch == 3:
        name=input("enter the name:")
        m1=int(input("enter the m1:"))
        my_col.update_one({"name":name},{"$set":{"m1":m1}})

    if ch == 4:
        name = input("enter the name:")
        my_col.delete_one({"name":name})

    if ch == 5:
        print("thank you")
        x=False






