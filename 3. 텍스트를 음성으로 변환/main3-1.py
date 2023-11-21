from gtts import gTTS
from playsound import playsound

class TextToSpeech:

    def __init__(self):
        self.text = ''
    def set_text(self,text):
        self.text = text  # 값이 다르기 때문에 동기화 하려는 것임. (연관성 無)
    def save_mp3(self,title):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"./{title}.mp3")


if __name__ == '__main__':
    t=TextToSpeech()
    title = input('제목을 입력')
    text = input('내용을 입력')
    t.set_text(text)
    t.save_mp3(title)

    playsound(f"./{title}.mp3")

