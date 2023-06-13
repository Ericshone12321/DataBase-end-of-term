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
    SELECT NAME
    FROM customer
    GROUP BY name
    HAVING SUM(bought_price) = 
    (SELECT MAX(cost) FROM (SELECT SUM(bought_price) AS cost FROM customer GROUP BY name) AS allcustomer)
    '''
)

for name in cursor.fetchall():
    print("The best customer is: %s" %name)

connection.commit()
cursor.close()
connection.close()