from bs4 import BeautifulSoup
import requests

class MelonMusic:
    def __init__(self):
        self.url = 'https://www.melon.com'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.class_name = []

    def set_url(self,url):
        self.url = requests.get(f'{self.url}/{time}', headers=self.headers).text

    def get_url(self):
        return self.url

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs=({"class":'ellipsis rank 01'}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        return self.title_ls


if __name__ == '__main__':
    m=MelonMusic()
    url=input('멜론에서 크롤링할 url을 입력하시오')
    # https://www.melon.com/chart/index.htm?dayTime=
    m.set_url(url)
    u2 = m.get_url()

    print(f'당신이 원하는 대상은 {u2} 입니다.')

    ls = m.get_ranking()

    print(f'최종단계 리스트 확인 {ls}')
