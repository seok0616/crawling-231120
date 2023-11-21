import qrcode

class QrMaker:
    def __init__(self):
        self.domain = ''
    def set_domain(self,domain):
        self.domain = domain
    def save_qrcode(self,title):
        qr_data = self.domain
        qr_img = qrcode.make(qr_data)


        save_path = f'./{title}.png'
        qr_img.save(save_path)

if __name__ == '__main__':
    q = QrMaker()
    domain = input('도메인 입력')
    q.set_domain(domain)
    title = input('파일명 입력')
    q.save_qrcode(title)
