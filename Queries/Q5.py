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
    SELECT company, track_id, brand, TYPE, contract_number
    FROM shipment
    WHERE track_id = 123456
    '''
)

for company, track_id, TYPE, brand, contract_number in cursor.fetchall():
    print("company: %s," %company, "Track_id: %d," %track_id, "content of lost shipment: %s %s," %(TYPE, brand), "Contract_number: %d" %contract_number)

connection.commit()
cursor.close()
connection.close()