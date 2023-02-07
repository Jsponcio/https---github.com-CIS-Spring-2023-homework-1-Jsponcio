# Jameria S Poncio
#  dbname: cis3368spDB, user: Jspon166, pass: 3368SP23
import mysql.connector
from mysql.connector import Error

#  Creation of SQL DB connection
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

#  Function to add cases to the DB
def addCases():
    country = input('Please enter the country name: ')
    #  making sure the inputs are ints so that they correcpond to the proper value type as the db
    year = int(input('Please enter the year: '))
    total = int(input('Please enter the total cases: '))
    deaths = int(input('Please enter the death count: '))
    recover = int(input('Please enter the number of people who recovered: '))
    # creating a dictionary to pull data from that is accessable in the mySQL syntax
    userInput = {
        'country': country,
        'year': year,
        'total': total,
        'deaths': deaths,
        'recover': recover
    }
    sql = ("INSERT INTO covidcases (countryname, year, totalcases, deaths, recovered) VALUES (%(country)s, %(year)s, %(total)s, %(deaths)s, %(recover)s)")
    cursor.execute(sql, userInput)

    con.commit() #  commiting changes to the DB

#  Function to output all of the cases in the DB
def outputCases():
    sql = 'select * from covidcases'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for covidcase in rows:
        print(covidcase)

#  connecting to the db with proper creditials
con = create_con('cis3368-25450-spring.cd5hir6sn816.us-east-1.rds.amazonaws.com', 'Jspon166', '3368SP23', 'cis3368spDB')

cursor = con.cursor(dictionary=True)

#  While loop menu function
while True:  
    print('\nMenu')  
    print('a - Add cases')  
    print('o - Ouput all cases')  
    print('q - Quit')  
    userchoice = input('\nEnter your choice:')
    userchoice = userchoice.lower() #  making the menu NOT case sensitive by turning all input into lowercase

    if userchoice == 'a':
        addCases()
    
    elif userchoice == 'o':
        outputCases()

    elif userchoice == 'q': # quit case to break loop
        print('\nGoodbye')
        break
    
    else: print('\nIncorrect/Invalid choice. Please choose again') #  setting up a loop to promt the user for a correct input