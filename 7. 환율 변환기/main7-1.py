from currency_converter import CurrencyConverter
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

if __name__ == '__main__':
    e = Exchange()
    while 1 :
        menu = input('0-종료, 1-전체화폐단위, 2-달러를 원화로')
        if menu == '0':
            print('프로그램 종료')
            break                   # 종료일 때는 break
        elif menu == '1':
            c = e.get_all_currencies()
            print(f'전체화폐 : {c}')
        elif menu == '2':
            c = e.change_usd_to_krw_currencies()
            print(f'변환된 결과 : {c}')
        else :
            print('메뉴에 없는 번호 입니다.')
            continue               # 다시 보여 줄 때 continue
