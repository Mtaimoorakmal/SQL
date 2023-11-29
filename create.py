print("hello world")
import sqlite3

connection = sqlite3.connect("sample.db")

table = 'CREATE TABLE People (id integer primary key , name TEXT , surmane TEXT)'
courser = connection.cursor()
courser.execute(table)
connection.commit()