#!/usr/bin/python3

import pymysql

def delOneData():
    sql = "TRUNCATE TABLE movies"
    cursor.execute(sql)

def delOneData():
    # 删除数据
    
    sql = "DELETE FROM movies WHERE movie = '倩女幽魂'"  # 删除倩女幽魂这条数据
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    

# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='test123', port=3306)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
#print('Database version:', data)
print("Database version : %s " % data)
# 关闭数据库连接
#db.close()

#创建数据库
try:
    cursor.execute("CREATE DATABASE movies DEFAULT CHARACTER SET utf8")
    print("creat database movies success!")
except:
    db.rollback()
    print("create database failed,perhaps already exists!")
    

#创建表
db = pymysql.connect(host='localhost', user='root', password='test123', port=3306, db='movies')
cursor = db.cursor()

try:
    sql = ('CREATE TABLE IF NOT EXISTS movies('
            'movie VARCHAR(255) NOT NULL,'
            'actor VARCHAR(255) NOT NULL,'
            'score VARCHAR(255) NOT NULL,'
            'realse VARCHAR(255) NOT NULL,'
            'PRIMARY KEY(movie)'
            ')'
           )
    cursor.execute(sql)
    db.commit()
    print("create table movies success!")
except:
    db.rollback()
    print("create table movies failed!")

#插入数据
movie = "倩女幽魂"
actor = "张国荣,王祖贤,午马"
score = "8.8"
realse = "2011-04-30"

sql = "INSERT INTO movies(movie,actor,score,realse) values(%s,%s,%s,%s)"

try:
    cursor.execute(sql, (movie, actor, score, realse))
    db.commit()
    print("insert data success!")
except:
    db.rollback()
    print("insert data failed!")


#打印数据
sql = "SELECT * FROM movies"

try:
    cursor.execute(sql)
    data = cursor.fetchone()
    while data:
        print(data)
        data = cursor.fetchone()
except:
    print("Error!")
    
#db.close()

#更新数据

sql = 'UPDATE movies SET score = %s WHERE movie = %s'

try:
    cursor.execute(sql, ('9,9', '倩女幽魂'))
    db.commit()
    print("update data success!")
except Exception as e:
    print("update data failed!!")
    print('error', e)
    #traceback.print_exc()
    db.rollback()


#delAllData()
#show all data
sql = "SELECT * FROM movies"

cursor.execute(sql)
data = cursor.fetchall()
print(data)
db.close()

