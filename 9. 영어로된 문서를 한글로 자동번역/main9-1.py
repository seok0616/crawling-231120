import googletrans


# pip install googletrans==4.0.0-rc1

class Translater:

    def __init__(self):
        self.translator = googletrans.Translator()
        self.text = ''

    def set_text(self, text):
        self.text = text

    def en_to_kr(self):
        result2 = self.translator.translate(self.text, dest='ko', src='en')
        return result2
        # print(f"I am happy => {result2.text}")

    def kr_to_en(self):
        result1 = self.translator.translate(self.text, dest='en', src='auto')  # print(f"행복하세요 => {result1.text}")
        return result1


    def en_doc_to_kr(self):
        read_file_path = r"./영어파일.txt"
        write_file_path = r"./한글파일.txt"

        with open(read_file_path, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result1 = self.translator.translate(lines, dest='ko')
            print(result1.text)
            with open(write_file_path, 'a', encoding='UTF8') as f:
                f.write(result1.text + '\n')


if __name__ == '__main__':
    t = Translater()
    while 1:
        menu = input('0-종료, 1-입력하세요, 2-영어에서 한글, 3-한글에서 영어,4-영어문서 한글로')
        if menu == '0':
            print('프로그램 종료')
            break  # 종료일 때는 break
        elif menu == '1':
            text = input('문장을 입력')  # 하나
            t.set_text(text)
        elif menu == '2':
            a = t.en_to_kr()
            print(f'결과는 {a}')
        elif menu == '3':
            a = t.kr_to_en()
            print(f'결과는 {a}')
        elif menu == '4':
            a = t.en_doc_to_ko
            print(f'결과는 {a}')
        else:
            print('메뉴에 없는 번호 입니다.')
            continue  # 다시 보여 줄 때 continue
