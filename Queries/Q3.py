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
    SELECT DISTINCT *
    FROM (
    SELECT brand, type FROM storage WHERE shop = "Kaohsiung1" AND is_empty = "yes"
    UNION
    SELECT brand, type FROM storage WHERE shop = "Kaohsiung2" AND is_empty = "yes"
    ) AS lack
    order BY brand
    '''
)

for brand, type in cursor.fetchall():
    print(brand, type)

connection.commit()
cursor.close()
connection.close()