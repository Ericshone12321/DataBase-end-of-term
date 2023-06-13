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
    SELECT company, track_id, TYPE, brand
    FROM shipment
    WHERE is_on_time = "no"
    '''
)

for company, track_id, TYPE, brand in cursor.fetchall():
    print("company: %s," %company, "ID: %d," %track_id, "product: %s %s" %(TYPE, brand))

connection.commit()
cursor.close()
connection.close()