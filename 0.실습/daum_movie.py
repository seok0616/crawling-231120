import requests
import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs
class DaumMovie:

    def __init__(self):
        self.url=''
        self.count = None  # 숫자인지 문자인지 명확하지 않은경우 None으로 정의 숫자일경우 '0', 문자일경우 '' # 크롤링 결과
        self.review_count = 0
        self.review_list = []

    def set_url(self,url):
        self.url = url

    def set_count(self):
        res = req.get(self.url)
        movie_code = '149761585'
        count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
        count_res = req.get(count_url)
        count_json = json.loads(count_res.text)
        self.count = count_json
        return self.count # 로직상 필요는 없지만 main 에서 print 하기 위해 리턴 함

    def extract_count(self):
        self.review_count = self.count['count'] # {'count': 287, 'sum': 1118, 'id': 149761585}
        return self.review_count

    def set_review_list(self):
        for i in range(0,1): #. self.review_count가 맞는데 시간 관계상
            res = requests.get(self.url) # request는 get 이다. 실용사례 많음.
            ls = json.loads(res.text)
            print(f' i값 : {ls}')
            for i, _ in enumerate(ls):
                review = ls[i]['content']
                user = ls[i]['user']['displayName']
                rating = ls[i]['rating']
                self.review_list.append([user,rating,review])
            df = pd.DataFrame(self.review_list, columns={'user','rating','review'})
            df.to_excel('./data/daum_review.xlsx')

if __name__ == '__main__':
    d = DaumMovie()
    while 1:
        menu = input('0-종료, 1-url 등록, 2-리뷰갯수, 3-리뷰목록')
        if menu == '0':
            print ('프로그램 종료')
            break

        elif menu == '1':
            # url = input('url을 입력하세요.') #원래는 수동으로 입력해야하는데 편의상 자동 입력으로 대체
            url2 = 'https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
            d.set_url(url2)

        elif menu == '2':
            d.set_count()
            c = d.extract_count()
            print(f'리뷰의 총 갯수{c}')

        elif menu == '3':
            d.set_review_list()

        else:
            print ('잘못된 번호')
            continue
