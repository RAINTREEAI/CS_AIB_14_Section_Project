import pandas as pd
import psycopg2

def read_vtgwxcqn_DB():
    # URL : postgres://vtgwxcqn:sSIui0RBGN3CPwxx5CL59r8RYZ_fl1TB@arjuna.db.elephantsql.com/vtgwxcqn
    # URL : postgres://qvuafktk:LdetCHWFFCBBmPrYzjYR_n2NOnPKpCsg@arjuna.db.elephantsql.com/qvuafktk
    host = 'arjuna.db.elephantsql.com'
    user = 'vtgwxcqn'
    password = 'sSIui0RBGN3CPwxx5CL59r8RYZ_fl1TB'
    database = 'vtgwxcqn'

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cur = connection.cursor()
    cur.execute("SELECT * FROM usedbook")
    data = cur.fetchall()
    df = pd.DataFrame(data)
    columns = ['itemId', 'title', 'link', 'author', 'pubDate', 'isbn', 'priceSales', 'priceStandard', 'cover', 
                'categoryId', 'categoryName', 'publisher', 'salesPoint', 'adult', 'ReviewRank', 'bestRank']
    df.columns = columns
    connection.commit()
    cur.close()
    connection.close()
    #df['pubDate'] = df['pubDate'].apply(lambda x: x.strftime('%Y%m%d'))

    return df

def read_qvuafktk_DB():
    # URL : postgres://vtgwxcqn:sSIui0RBGN3CPwxx5CL59r8RYZ_fl1TB@arjuna.db.elephantsql.com/vtgwxcqn
    # URL : postgres://qvuafktk:LdetCHWFFCBBmPrYzjYR_n2NOnPKpCsg@arjuna.db.elephantsql.com/qvuafktk

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

    cur = connection.cursor()
    cur.execute("SELECT * FROM usedbook")
    data = cur.fetchall()
    df = pd.DataFrame(data)
    columns = ['itemId', 'title', 'link', 'author', 'pubDate', 'isbn', 'priceSales', 'priceStandard', 'cover', 
                'categoryId', 'categoryName', 'publisher', 'salesPoint', 'adult', 'ReviewRank', 'bestRank']
    df.columns = columns
    connection.commit()
    cur.close()
    connection.close()
    #df['pubDate'] = df['pubDate'].apply(lambda x: x.strftime('%Y%m%d'))

    return df
