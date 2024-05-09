from connection import connect
from crud import *

def main():
                                            # connecting to db server
    con=connect("phonebook",'localhost',5648)
                                            # read records of a table in phonebook database
    read(con,'person')
                                            # insert a record in phonebook databse
    # insert(con,'person','name,email,personid',"'reza','rezarezaee@gmail.com','0024403474'")
    # read(con,'person')
                                            # update a row in phonebook database
    # update(con,'person','name','reyhane','name','reza')
    # read(con,'person')
                                            # delete a record in phonebook database
    # delete(con,'person','name','reyhane')
    # read(con,'person')

if __name__=="__main__":
    main()