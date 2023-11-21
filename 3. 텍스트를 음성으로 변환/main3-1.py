from gtts import gTTS

class TextToSpeech:

    def __init__(self):
        self.text = ''
    def set_text(self,text):
        self.text = text  # 값이 다르기 때문에 동기화 하려는 것임. (연관성 無)
    def save_mp3(self,title):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"./{title}.mp3")

if __name__ == '__main__':

    t = TextToSpeech
    title = input('제목을 입력하시오')
    text = input('변환하려는 문장을 입력하시오')
    t.set_text(text)
    t.save_mp3(title)

    playsound("./hi.mp3")