#  dbname: cis3368spDB, user: Jspon166, pass: 3368SP23
#  Menu a – Add cases o – Output all cases in console q – Quit
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

def addCases():
    country = input('Please enter the country name: ')
    year = int(input('Please enter the year: '))
    total = int(input('Please enter the total cases: '))
    deaths = int(input('Please enter the death count: '))
    recover = int(input('Please enter the number of people who recovered: '))
    userInput = {
        'country': country,
        'year': year,
        'total': total,
        'deaths': deaths,
        'recover': recover
    }
    sql = ("INSERT INTO covidcases (countryname, year, totalcases, deaths, recovered) VALUES (%(country)s, %(year)s, %(total)s, %(deaths)s, %(recover)s)")
    cursor.execute(sql, userInput)

    con.commit()

def outputCases():
    sql = 'select * from covidcases'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for covidcase in rows:
        print(covidcase)


con = create_con('cis3368-25450-spring.cd5hir6sn816.us-east-1.rds.amazonaws.com', 'Jspon166', '3368SP23', 'cis3368spDB')

cursor = con.cursor(dictionary=True)


while True:  
    print('\nMenu')  
    print('a - Add cases')  
    print('o - Ouput all cases')  
    print('q - Quit')  
    userchoice = input('\nEnter your choice:')
    userchoice = userchoice.lower()

    if userchoice == 'a':
        addCases()
    
    elif userchoice == 'o':
        outputCases()

    elif userchoice == 'q':
        print('\nGoodbye')
        break
    
    else: print('\nIncorrect/Invalid choice. Please choose again')