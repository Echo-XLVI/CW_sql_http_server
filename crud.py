from connection import connect
def insert(connection:object,table_name:str,columns:str,values:str):
    try:
        cursor=connection.cursor()
        query=f"insert into {table_name} ({columns}) values ({values})"
        cursor.execute(query)
        connection.commit()
        print(cursor.rowcount)
    except Exception as error:
        print(error)
        raise Exception
    
def read(connection:object,table_name:str) -> None:
    cursor=connection.cursor()
    cursor.execute(f"select * from {table_name}")
    records=cursor.fetchall()
    for row in records:
        print(row)

def update(connection:object,table_name:str,column_name:str,new_value:str,condition_col:str,condition_val:str):
    try:
        cursor=connection.cursor()
        query=f"""update {table_name} set {column_name}='{new_value}' where {condition_col}='{condition_val}'"""
        cursor.execute(query)
        connection.commit()
    except Exception:
        raise Exception

def delete(connection:object,table_name:str,column_name:str,value:str):
    try:
        cursor=connection.cursor()
        cursor.execute(f"delete from {table_name} where {column_name}='{value}'")
        connection.commit()
        return cursor.rowcount
    except Exception:
        raise Exception



# con=Connection.connect("phonebook",'localhost','postgres','1380ACreZA46',5648)
                                        # read records of a table in phonebook database
# read(con,'person')
                                        # insert a record in phonebook databse
# insert(con,'person','name,email,personid',"'reza','rezarezaee@gmail.com','0024403474'")
# read(con,'person')
                                        # update a row in phonebook database
# update(con,'person','name','reyhane','name','reza')
# read(con,'person')
                                        # delete a record in phonebook database
# delete(con,'person','name','reyhane')
# read(con,'person')