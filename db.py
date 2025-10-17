from sqlite3 import connect, Error


def Maxsulotlar():
    try:
        c = connect("maxsulot.db")
        cursor = c.cursor()
        cursor.execute("select * from maxsulot")
        malumotlar = cursor.fetchall()
        return malumotlar
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if c:
            cursor.close()
            c.close()




# def MaxsulotAdd(name, price, image, dec):
#     try:
#         c = connect("maxsulot.db")
#         cursor = c.cursor()
#         cursor.execute("""
#            insert into maxsulot(name, price, image, dec) values(?, ?, ?, ?)
#             """, (name, price, image, dec))
#         c.commit()
#         return "bajarildi"
#     except (Exception, Error) as error:
#         print("Xato", error)
#     finally:
#         if c:
#             cursor.close()
#             c.close()


# name = input("nomi: ")
# price = float(input("narxi: "))
# image = input("rasm: ")
# dec = input("xaqida: ")
# print(MaxsulotAdd(name, price, image, dec))











# try:
#     c = connect("maxsulot.db")
#     cursor = c.cursor()
#     cursor.execute("""
#         Create table karzinka(
#                    id integer primary key not null,
#                    user_id int unique,
#                    name text not null,
#                    price real not null,
#                    count int not null
#                    );
#         """)
#     c.commit()
# except (Exception, Error) as error:
#     print("Xato", error)
# finally:
#     if c:
#         cursor.close()
#         c.close()








# try:
#     c = connect("maxsulot.db")
#     cursor = c.cursor()
#     cursor.execute("""
#         Create table maxsulot(
#                    id integer primary key not null,
#                    name text not null,
#                    price real not null,
#                    image text not null,
#                    dec text not null
#                    );
#         """)
#     c.commit()
# except (Exception, Error) as error:
#     print("Xato", error)
# finally:
#     if c:
#         cursor.close()
#         c.close()






# try:
#     c = connect("maxsulot.db")
#     cursor = c.cursor()
#     cursor.execute("""
#         Create table users(
#                    id integer primary key not null,
#                    user_id int unique,
#                    name text not null,
#                    username text
#                    );
#         """)
#     c.commit()
# except (Exception, Error) as error:
#     print("Xato", error)
# finally:
#     if c:
#         cursor.close()
#         c.close()