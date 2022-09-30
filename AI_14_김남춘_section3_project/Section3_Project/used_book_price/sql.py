import psycopg2

def dbcon():
    host = 'arjuna.db.elephantsql.com'
    user = 'qvuafktk'
    password = 'LdetCHWFFCBBmPrYzjYR_n2NOnPKpCsg'
    database = 'qvuafktk'

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def create_table():
    conn = dbcon()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS usersearch (
                    title           VARCHAR,
                    pubDate         INT,
                    priceStandard   INT,
                    ReviewRank      INT,
                    pricePredict    INT)
                """)
    conn.commit()
    conn.close()

def insert_data(title, pubDate, priceStandard, ReviewRank, pricePredict):
    conn = dbcon()
    cur = conn.cursor()
    setdata = (title, pubDate, priceStandard, ReviewRank, pricePredict)
    cur.execute("INSERT INTO usersearch VALUES (%s, %s, %s, %s, %s)", setdata)
    conn.commit()
    cur.close()
    conn.close()