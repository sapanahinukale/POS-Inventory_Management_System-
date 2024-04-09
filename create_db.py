import sqlite3
def create_db():
    con=sqlite3.connect(database=r'pos.db')
    cur=con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name varchar,contact int(10),desc text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name varchar)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier varchar,Category text,name varchar,price int,qty int,status text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name varchar,email text,gender text,contact int(10) ,dob date,doj date,pass text,utype text,address text,salary int)")
    con.commit()
    
    
   

    


   
    

create_db()
              