from flask import Flask, render_template, request
from used_book_price import getAPI, sql
import pickle

def create_app():
    
    with open('used_book_price/model_pickle/model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)
    app = Flask(__name__)

    # 한글 깨짐 방지
    app.config['JSON_AS_ASCII'] = False

    # 메인 페이지 라우팅
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # 도서 검색 페이지 라우팅
    @app.route('/search')
    def search():
        return render_template('search.html')

    # 도서 겸색 결과 처리
    @app.route('/search/result', methods = ['POST', 'GET'])
    def result():
        keyword = str(request.args.get('keyword'))
        bookInfo = getAPI.getSearchBook(keyword)
            
        return render_template('result.html', info=bookInfo)

    # 직접 입력 페이지 라우팅
    @app.route('/direct')
    def direct():
        return render_template('direct.html')

    # 검색 > 데이터 예측 처리
    @app.route('/predict', methods=['POST'])
    def search_pred():
        data1 = request.form['pubDate']
        data2 = request.form['priceStandard']
        data3 = request.form['ReviewRank']
        data4 = request.form['title']
        arr = [[int(data1), int(data2), int(data3)]]
        pred = model.predict(arr)
        sql.create_table()
        sql.insert_data(data4, data1, data2, data3, int(pred.round(-2)))

        return render_template('predict.html', data=int(pred.round(-2)))

    # 직접 입력 > 데이터 예측 처리
    @app.route('/predict', methods=['POST'])
    def pred():
        data1 = request.form['pubDate']
        data2 = request.form['priceStandard']
        data3 = request.form['ReviewRank']
        data4 = request.form['title']
        arr = [[int(data1), int(data2), int(data3)]]
        pred = model.predict(arr)
        sql.create_table()
        sql.insert_data(data4, data1, data2, data3, int(pred.round(-2)))

        return render_template('predict.html', data=int(pred.round(-2))), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)