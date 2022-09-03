#This is my first python code
"""
This is another way to comment
"""
if 5>3:
    print("hello world!")
if 8 > 1 :
    print("Nice");
x,y,z = "Rathina",'is',"Smart"
print(x,y,z)


def func():
    global z
    z="happy"
    print("I'm "+z)

func()
print(x,y,z)

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

