from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup
# pip install CurrencyConverter

class Exchange:
    def __init__(self):
        pass

    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw_currencies(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1,'USD','KRW')

    def realtime_usd_to_krw(self,target1, target2):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
        # https://kr.investing.com/currencies/usd-krw
        response = requests.get(f"https://kr.investing.com/currencies/{target1}-{target2}", headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find(name = 'span',attrs = {'data-test': 'instrument-price-last'})
        for 1 in ls:

        # return containers.text

if __name__ == '__main__':
    e = Exchange()
    while 1 :
        menu = input('0-종료, 1-전체화폐단위, 2-달러를 원화로, 3-실시간 환율변환')
        if menu == '0':
            print('프로그램 종료')
            break                   # 종료일 때는 break
        elif menu == '1':
            c = e.get_all_currencies()
            print(f'전체화폐 : {c}')
        elif menu == '2':
            c = e.change_usd_to_krw_currencies()
            print(f'변환된 결과 : {c}')
        elif menu == '3':
            target1 = input('바꾸려는 화폐단위:')
            target2 = input('바뀌는 화폐단위:')
            c = e.realtime_usd_to_krw('USD','KRW')
            print(f'변환된 결과 : {c}')


        else :
            print('메뉴에 없는 번호 입니다.')
            continue               # 다시 보여 줄 때 continue
