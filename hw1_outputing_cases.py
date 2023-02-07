import mysql.connector
from mysql.connector import Error

def create_con(hostname, uname, pwd, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname, 
            user = uname,
            password = pwd,
            database = dbname
        )
    except Error as e:
        print('Error is :', e)
    return connection

def outputCases():
    sql = 'select * from covidcases'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for covidcase in rows:
        print(covidcase)


con = create_con('cis3368-25450-spring.cd5hir6sn816.us-east-1.rds.amazonaws.com', 'Jspon166', '3368SP23', 'cis3368spDB')

cursor = con.cursor(dictionary=True)