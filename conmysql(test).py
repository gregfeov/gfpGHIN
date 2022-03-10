from mysql.connector import connect, Error
#from der import *
import time

def allvalues():
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
                cursor.execute("SELECT * from tt")
                row = cursor.fetchone()
                while row is not None:
                    print(row)
                    row = cursor.fetchone()
    except Error as e:
        print(e)
allvalues()
def check():
    try:
        with connect(
            host="localhost",
            user="root",
            password="93029302",
        ) as connection:
            a=rh()
            if connection.is_connected():
                print("Connected to database")
            time.sleep(1)
            print(a)
            with connection.cursor() as cursor:
                cursor.execute("USE gfpdb")
            
                cursor.execute("SELECT address FROM tt WHERE address='"+a+"'")
                row = cursor.fetchone()
                if row==None:
                    cursor.execute("INSERT INTO tt(address,balance) VALUES('"+a+"','"+str(100)+"')")
                    connection.commit()
                    print("Token created successfully with start balance 100")
                else:
                    print("Token is alredy created!")
    except Error as e:
        print(e)
