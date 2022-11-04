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
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.widget import Widget
from kivymd.uix.label import MDLabel
from test.parser.parser import GPZU_parser
from kivymd.uix.button import MDRaisedButton





Window.size = (720, 1024)


class ScreenManagement(ScreenManager):
    pass

class PageUploadFile(Screen):
    pass
    
class PageAllFile(Screen):
    pass


class PageResult(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows = 1
        self.size_hint = (1, 1)
        # self.size_x = 100000
        # self.size_y = 100000
        self.bind(minimum_width=self.setter('width'))


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_x = 1
        self.size_hint_y = 1
        self.bind(minimum_width=self.setter('width'))




class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.arrayPath=[]
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            selector='multi'
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

    def result_page_exit_callbak(self, name_page = 'PageAllFile'):
        self.root.ids.manager.current = name_page

    def getTableResult(self):

        listColumn = []
        rowData = []
        
        for i in range(len(self.arrayPath)):
            p = GPZU_parser(files_paths=[self.arrayPath[i]])
            data = p.parse()
            dataKeys = data.keys()
            nameColumn = list(data.get(list(dataKeys)[0]).keys())
            if len(listColumn) == 0:
                for i in range(len(nameColumn)):
                    listColumn.append((nameColumn[i], dp(100)))
            
            for i in range(len(data)):
                row = [str(i), list(dataKeys)[i]]
                for g in range(len(nameColumn)-2):
                    row.append(data.get(list(dataKeys)[i]).get(nameColumn[g+2]))
                rowData.append(tuple(row))
            

        data_tables = MDDataTable(
            rows_num=100,
            use_pagination=True,
            column_data=listColumn,
            row_data=rowData,
            # sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        return data_tables

    

    def openPageResult(self):
        self.root.ids.boxResult.clear_widgets()
        base = FloatLayout(
            size_hint = (1, 1)
        )  
        button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5, 'top': 0},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )
        button_box.add_widget(MDRaisedButton(text="export"))
        box = MyBox()
        box.add_widget(Widget(size_hint_y=0))
        box.add_widget(Widget(size_hint_y=0))
        box.add_widget(self.getTableResult())
        scroll = ScrollView(do_scroll_y=False, pos_hint={"center_y": .5})
        scroll.add_widget(box)
        base.add_widget(scroll)
        base.add_widget(ScrollView())
        base.add_widget(button_box)
        self.root.ids.boxResult.add_widget(base)



    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


MyApp().run()