import pymysql

db = pymysql.connect(host='192.168.155.101', user='hypark', password='parkhy0115!', port=4567, db='madang', charset='utf8')

cursor = db.cursor()

while 1:
    print("-------------------------------------------")
    print("[2020069022]------------[Hyeong-Yeong Park]")
    print("[------Bookstore Management System--------]")
    print("[1] Insert book")
    print("[2] Delete book")
    print("[3] Search Book")
    print("[4] Print book DB")
    print("[5] Exit")
    menu = int(input())
    if menu == 1:
        sql = "INSERT INTO Book (bookid, bookname, publisher, price) VALUES (%s, %s, %s, %s)"
        print("Input the book's information that you want to insert (bookid, bookname, publisher, price: )")
        bookid = int(input())
        bookname = str(input())
        publisher = str(input())
        price = int(input())
        cursor.execute(sql, (bookid, bookname, publisher, price))
    elif menu == 2:
        sql = "DELETE FROM Book WHERE bookname = %s"
        print("Input the book's name that you want to delete: ")
        deleteBookname = str(input())
        cursor.execute(sql, deleteBookname)
        db.commit()
    elif menu == 3:
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("Search for (book's name) :")
        searchBook = str(input())
        cursor.execute(sql, searchBook)
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif menu == 4:
        sql = "SELECT * FROM Book"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    elif menu == 5:
        break

    db.commit()