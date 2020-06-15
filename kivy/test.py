
from kivy.app import App
from kivy.uix.label import Label #导入标签类

class TestApp(App): 
    def build(self): 
        return Label(text='Hello Kivy!') #定义标签文本
 
TestApp().run()