from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video(source='/Users/aluno.sesipaulista/Downloads/Just Cause 2 - Bolo Santosi Intro.mp4')
    
if __name =="__main__":
    MinhaApp().run()
