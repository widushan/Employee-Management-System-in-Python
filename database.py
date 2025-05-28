import pymysql
from tkinter import messagebox


def connect_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host="localhost",user="root",password="root")
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Database connection failed')
        return
    
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(10), Name VARCHAR(50), Phone VARCHAR(20), Role VARCHAR(30), Gender  VARCHAR(10), Salary DECIMAL(10,2))')



def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()
    


def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0


def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result=mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s, phone=%s, role=%s, gender=%s, salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()


def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()


def search(option, value):
    query = f"SELECT * FROM data WHERE `{option}` = %s"
    mycursor.execute(query, (value,))
    result = mycursor.fetchall()
    return result


def deleteall_records():
    mycursor.execute('DELETE FROM data')
    conn.commit()


connect_database()