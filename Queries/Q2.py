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
    SELECT YEAR,brand,type,SUM(income)AS allincome
    FROM sale_data
    GROUP BY TYPE,brand
    ORDER BY allincome DESC LIMIT 2
    '''
)

for year, brand, type, allincome in cursor.fetchall():
    print("year: %s," %year, "product: %s %s," %(brand, type),"income: %d" %allincome)

connection.commit()
cursor.close()
connection.close()