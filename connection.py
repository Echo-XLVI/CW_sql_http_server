import threading
import psycopg2
from psycopg2 import Error
import time

# def authentication(func):
#     def wrapper(*args):
#         print(*args)
#         user=input("Enter your username:")
#         password=input('Enter db password:')        
#         func(*args,user,password)
#     return wrapper

# @authentication
def connect(dbname:str,host:str,port:int,user:str=None,password:str=None) -> object:
    counter=0
    con=None
    enter_time = recent_time = time.time()
    while counter<15 and recent_time-enter_time<60:
        try:              
            con=psycopg2.connect(dbname=dbname,host=host,user=user,password=password,port=port)
            cursor=con.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(con.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")                        
        except (Exception, Error) as error:
                print("Error while connecting to PostgreSQL", error)
        finally:
            if con!=None:
                cursor.close()
                return con
            else:
                counter+=1
                recent_time=time.time()
                print(counter)
                print(recent_time-enter_time)

                                    # muilti threading 
# def timer():
#     pass


# def connect(dbname:str,host:str,user:str,password:str,port:int):
#     try:
#         t1 = threading.Thread(target=timer, args=(10,))
#         t2 = threading.Thread(target=connect, args=(10,))
 
#         t1.start()
#         t2.start()

#         t1.join()
#         t2.join()
#     except Exception as error:
#         print(error)

