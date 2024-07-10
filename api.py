import sqlite3
import requests as rq
ure = 'https://dummyjson.com/products'
file = rq.get(ure).json()


def cread_read():
    con=sqlite3.connect('first.db')
    cursor = con.cursor()

    table = '''SELECT * FROM JSON'''
    cursor.execute(table)
    a = cursor.fetchall()
    con.commit()
    return a

   
def cread_add(id, title, price, img, disc):
    try:
        con = sqlite3.connect('first.db')
        cursor = con.cursor()

        table='''INSERT INTO JSON(PRODUCT_ID,PRODUCT_NAME,PRICE,PICTURE,DISC) VALUES (?,?,?,?,?)'''
        cursor.execute(table,(id, title, price, img, disc,))

        con.commit()
    except sqlite3.Error as error:
        print(error)

def delet(NAME):
    try:
        con = sqlite3.connect('first.db')
        cur = con.cursor()
        add = '''
            DELETE FROM JSON WHERE PRODUCT_NAME = ?
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




# for i in file['products']: 
#     id= i['id']
#     title= i['title']
#     img=i['images'][0]
#     desc=i['description']
#     price=i['price']
#     cread_add(id,title,img,desc,price)

# def creat():
#     try:
#         con=sqlite3.connect('first.db')
#         cursor=con.cursor()

#         table='''CREATE TABLE JSON(
#             PRODUCT_ID BIGINT NOT NULL,
#             PRODUCT_NAME VARCHAR(50) NOT NULL,
#             PRICE INTEGER NOT NULL,
#             PICTURE TEXT NOT NULL,
#             DISC TEXT NOT NULL
#         );'''
#         cursor.execute(table)

#         con.commit()
#         cursor.close()
#     except (Exception,sqlite3.Error) as eror:
#         print(eror)

#     finally:
#         if con:
#             con.close

# creat()