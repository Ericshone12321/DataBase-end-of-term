import mariadb

connection = mariadb.connect(
    user = "411077011",
    password = "411077011",
    host = "140.127.74.226",
    database = "411077011"
)
cursor = connection.cursor()

cursor.execute(
    '''
    select * from physical_shop
    '''
)

print("row number is:", cursor.rowcount)

connection.commit()
cursor.close()
connection.close()