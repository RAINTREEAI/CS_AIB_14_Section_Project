import requests
import json

def getUsedList():
    #api Key
    TTBKey = "ttbraintree10101841001"
    # QueryType : 신간 전체
    # SearchTarget : 중고
    # SubSearchTarget : 도서
    # MaxResults : n개 출력
    # start : i page부터
    # output : json
    # OptResult : 해당 상품에 등록된 중고상품 정보
    book_list = []
    QueryType = ['ItemNewAll', 'Bestseller']
    for query in QueryType:
        url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={TTBKey}&QueryType={query}&SearchTarget=Used" \
            "&SubSearchTarget=Book&start=1&MaxResults=50&output=js&Version=20131101&OptResult=usedList"
        print(query)
        res = requests.get(url)
        items = json.loads(res.text)['item']

        # itemId 아이디
        # title 제목
        # link 결과와 관련된 알라딘 페이지
        # author 지은이
        # pubDate 출판일
        # isbn isbn코드
        # priceSales 판매가
        # priceStandard 정가
        # cover 커버
        # categoryId 카테고리 아이디
        # categoryName 카테고리 이름
        # publisher 출판사
        # salesPoint 판매지수
        # adult 성인 등급 여부
        # customerReviewRank 회원리뷰평점
        # bestRank 베스트셀러 순위 정보
        # usedList < aladinUsed < itemCount 알라딘 직접 배송 보유 상품수
        # usedList < aladinUsed < minPrice 알라딘 직접 배송 최저가
        # usedList < userUsed< itemCount 회원 직접 배송 보유 상품수
        # usedList < userUsed< minPrice  회원 직접 배송 최저가
        for i in items:
            book_dict = {}
            book_dict['itemId'] = i['itemId']
            book_dict['title'] = i['title'][5:]
            book_dict['link'] = i['link']
            book_dict['author'] = i['author'].split(',')[0].split('(')[0]
            book_dict['pubDate'] = i['pubDate']
            book_dict['isbn'] = i['isbn']
            book_dict['priceSales'] = i['priceSales']
            book_dict['priceStandard'] = i['priceStandard']
            book_dict['cover'] = i['cover']
            book_dict['categoryId'] = i['categoryId']
            book_dict['categoryName'] = i['categoryName'].split('>')[3] if len(i['categoryName'].split('>')) > 3 else "None"
            book_dict['publisher'] = i['publisher']
            book_dict['salesPoint'] = i['salesPoint']
            book_dict['adult'] = 1 if i['adult'] == 'true' else 0
            book_dict['customerReviewRank'] = i['customerReviewRank']
            try:
                book_dict['bestRank'] = i['bestRank']
            except:
                book_dict['bestRank'] = 0
            #book_dict['aladin_itemCount'] = i['subInfo']['usedList']['aladinUsed']['itemCount']
            #book_dict['aladin_minPrice'] = i['subInfo']['usedList']['aladinUsed']['minPrice']
            #book_dict['user_itemCount'] = i['subInfo']['usedList']['userUsed']['itemCount']
            #book_dict['user_minPrice'] = i['subInfo']['usedList']['userUsed']['minPrice']

            book_list.append(book_dict)
    
    length = len(book_list)
    print(f"총 {length}개의 데이터가 수집되었습니다.")
    return book_list


def getSearchBook(keyword):
    #api Key
    TTBKey = "ttbraintree10101841001"
    book_search = []
    # QueryType : 신간 전체
    # SearchTarget : 중고
    # SubSearchTarget : 도서
    # MaxResults : 50개 출력
    # start : i page부터
    # output : json
    # OptResult : 해당 상품에 등록된 중고상품 정보
    url = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={TTBKey}&Query={keyword}&QueryType=Keyword&MaxResults=1&start=1&SearchTarget=Book&output=js&Version=20131101"
    
    res = requests.get(url)
    items = json.loads(res.text)['item']
    
    # itemId 아이디
    # title 제목
    # link 결과와 관련된 알라딘 페이지
    # author 지은이
    # pubDate 출판일
    # isbn isbn코드
    # priceSales 판매가
    # priceStandard 정가
    # stockstatus 재고상태
    # cover 커버
    # categoryId 카테고리 아이디
    # categoryName 카테고리 이름
    # publisher 출판사
    # salesPoint 판매지수
    # adult 성인 등급 여부
    # customerReviewRank 회원리뷰평점
    # bestRank 베스트셀러 순위 정보
    # usedList < aladinUsed < itemCount 알라딘 직접 배송 보유 상품수
    # usedList < aladinUsed < minPrice 알라딘 직접 배송 최저가
    # usedList < userUsed< itemCount 회원 직접 배송 보유 상품수
    # usedList < userUsed< minPrice  회원 직접 배송 최저가
    for item in items:
        book_dict = {}
        book_dict['title'] = item['title']
        book_dict['author'] = item['author'].split(',')[0].split('(')[0]
        book_dict['pubDate'] = item['pubDate']
        book_dict['cover'] = item['cover']
        book_dict['priceStandard'] = item['priceStandard']
        book_dict['categoryName'] = item['categoryName'].split('>')[3] if len(item['categoryName'].split('>')) > 3 else item['categoryName'].split('>')[2]
        book_dict['publisher'] = item['publisher']
        book_dict['salesPoint'] = item['salesPoint']
        book_dict['customerReviewRank'] = item['customerReviewRank']
        try:
            book_dict['bestRank'] = item['bestRank']
        except:
            book_dict['bestRank'] = 0

        book_search.append(book_dict)

    return book_search

    return book_search
