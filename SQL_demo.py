import mysql.connector

def Demo():
    cnx = mysql.connector.connect(user='root', password='root1234',
                              host='127.0.0.1',
                              database='mathematica_centrum')

    cursor = cnx.cursor()

    query = ("SELECT ID, content FROM questions WHERE ID < %d" % 10)

    cursor.execute(query)

    for (ID, content) in cursor:
      print("No. %d \n %s" % (ID, content))

    cursor.close()

    cnx.close()
