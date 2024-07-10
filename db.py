import sqlite3

def create_read():
    connection=sqlite3.connect('first.db')

    cursor=connection.cursor()

    table='''SELECT * FROM FIRST'''
    cursor.execute(table)
    a=cursor.fetchall()
    connection.commit()
    return a

def create_add(id,name,price,son):
    connection=sqlite3.connect('first.db')

    cursor=connection.cursor()

    table='''INSERT INTO FIRST(USER_ID,NAME,PRICE,SONI) VALUES (?,?,?,?)'''
    cursor.execute(table,(id,name,price,son))

    connection.commit()
# create_add(554507627, 'my_id', 555, 4)
def create():
    try:
        connection=sqlite3.connect('first.db')

        cursor=connection.cursor()

        table='''CREATE TABLE FIRST(
            USER_ID BIGINT NOT NULL,
            NAME VARCHAR(50) NOT NULL,
            PRICE GIGINT NOT NULL,
            SONI INTEGER NOT NULL
        );'''
        cursor.execute(table)

        connection.commit()
        cursor.close()
    except (Exception,sqlite3.Error) as eror:
        print(eror)
    finally:
        if connection:
            connection.close()


def delete(NAME):
    try:
        con = sqlite3.connect('first.db')
        cur = con.cursor()
        add = '''
            DELETE FROM FIRST WHERE NAME = ?
        '''
        cur.execute(add, (NAME,))
        con.commit()
        print('ishladi')
    except (Exception,sqlite3.Error) as er:
        print(er)
    finally:
        if con:
            cur.close()
            con.close()
            print('ilindi')



