from sched import scheduler
import psycopg2
import getAPI
from apscheduler.schedulers.blocking import BlockingScheduler



def caching():
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

    """
    itemId 아이디 INT
    title 제목 VARCHAR
    link 결과와 관련된 알라딘 페이지 VARCHAR
    author 지은이 VARCHAR
    pubDate 출판일 DATE
    isbn isbn코드 VARCHAR
    priceSales 판매가 INT
    priceStandard 정가 INT
    cover 커버 VARCHAR
    categoryId 카테고리 아이디 INT
    categoryName 카테고리 이름 VARCHAR
    publisher 출판사 VARCHAR
    salesPoint 판매지수 INT
    adult 성인 등급 여부 INT
    customerReviewRank 회원리뷰평점 INT
    bestRank 베스트셀러 순위 정보 INT
    usedList < aladinUsed < itemCount 알라딘 직접 배송 보유 상품수 INT
    usedList < aladinUsed < minPrice 알라딘 직접 배송 최저가 INT
    usedList < userUsed< itemCount 회원 직접 배송 보유 상품수 INT
    usedList < userUsed< minPrice  회원 직접 배송 최저가 INT
    """

    cur = connection.cursor()
    # cur.execute("DROP TABLE IF EXISTS usedbook")
    # print("기존 usedbook 테이블을 제거하였습니다.")
    cur.execute("""CREATE TABLE IF NOT EXISTS usedbook (
                    itemId          INT     UNIQUE NOT NULL     PRIMARY KEY,
                    title           VARCHAR,
                    link            VARCHAR,
                    author          VARCHAR,
                    pubDate         DATE,
                    isbn            VARCHAR,
                    priceSales      INT,
                    priceStandard   INT,
                    cover           VARCHAR,
                    categoryId      INT,
                    categoryName    VARCHAR,
                    publisher       VARCHAR,
                    salesPoint      INT,
                    adult           INT,
                    ReviewRank      INT,
                    bestRank        INT)
                """)

    connection.commit()
    #print("새로운 usedbook 테이블을 생성하였습니다.")

    # 중고책 리스트 데이터
    used_book_list = getAPI.getUsedList()

    sql = """INSERT INTO usedbook (itemId, title, link, author, pubDate, isbn, priceSales, priceStandard, cover, categoryId, categoryName,
     publisher, salesPoint, adult, ReviewRank, bestRank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
     ON CONFLICT (itemId) DO NOTHING"""
    # (itemId, title, link, author, pubDate, isbn, priceSales, priceStandard, cover, categoryId, categoryName, 
    # publisher, salesPoint, adult, ReviewRank, bestRank) 
    # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

    for i in range(len(used_book_list)):
        itemId = used_book_list[i]['itemId']
        title = used_book_list[i]['title']
        link = used_book_list[i]['link']
        author = used_book_list[i]['author']
        pubDate = used_book_list[i]['pubDate']
        isbn = used_book_list[i]['isbn']
        priceSales = used_book_list[i]['priceSales']
        priceStandard = used_book_list[i]['priceStandard']
        cover = used_book_list[i]['cover']
        categoryId = used_book_list[i]['categoryId']
        categoryName = used_book_list[i]['categoryName']
        publisher = used_book_list[i]['publisher']
        salesPoint = used_book_list[i]['salesPoint']
        adult = used_book_list[i]['adult']
        ReviewRank = used_book_list[i]['customerReviewRank']
        bestRank = used_book_list[i]['bestRank']
        # a_itemCount = used_book_list[i]['aladin_itemCount']
        # a_minPrice = used_book_list[i]['aladin_minPrice']
        # c_itemCount = used_book_list[i]['user_itemCount']
        # c_minPrice = used_book_list[i]['user_minPrice']

        val = (itemId, title, link, author, pubDate, isbn, priceSales, priceStandard, cover, categoryId, categoryName, publisher, 
                salesPoint, adult, ReviewRank, bestRank)

        cur.execute(sql,  val)

    print("데이터베이스에 데이터를 추가하였습니다.")

    connection.commit()
    cur.close()
    connection.close()

scheduler = BlockingScheduler({'apscheduler.timezone':'UTC'})
scheduler.add_job(func=caching, trigger='interval', seconds=60)

try:
    scheduler.start()
except KeyboardInterrupt:
    pass
