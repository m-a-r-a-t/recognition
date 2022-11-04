from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivy.properties import ObjectProperty




Window.size = (720, 1024)


class ScreenManagement(ScreenManager):
    pass

class PageUploadFile(Screen):
    pass
    

class PageAllFile(Screen):
    pass

    

class ContentNavigationDrawer(MDBoxLayout):
    pass



class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.arrayPath=[]
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def build(self):
        return Builder.load_file('my.kv')
    
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.arrayPath.append(path)
        print(path)
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
        print(self.arrayPath)
        self.afterExitManagerFile()

    def afterExitManagerFile(self):
        for i in range(len(self.arrayPath)):
            self.root.ids.pathUploadFileList.add_widget(
                ThreeLineListItem(text=f"File: {i}", secondary_text=f"Path: {self.arrayPath[i]}", tertiary_text=f"status: false")
            )


    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


DemoApp().run()