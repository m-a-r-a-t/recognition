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
from gpzu_parser.gpzu_parser import GPZU_parser
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import OneLineListItem
from app.db.model import *
from plyer import filechooser
from uuid import *
from kivy.properties import ListProperty




ui = """
Screen:
    MDNavigationLayout:

        ScreenManager:
            id: manager
            name: "Manager"
            
            PageUploadFile:
                name: "PageUploadFile"
                id: PageUploadFileScreen

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        
                        title: "Загрузить файлы"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None


                        MDRoundFlatIconButton:
                            text: "Выбрать файлы"
                            icon: "folder"
                            pos_hint: {'left': 0.3}
                        
                            on_release: app.file_manager_open()
                        
                        MDRoundFlatIconButton:
                            pos_y: "100"
                            text: "Результат"
                            icon: "file"
                            pos_hint: {'left': 0.6}
                            on_release: manager.current='PageResult' 
                            on_release: app.openPageResultAfterUpload()
                          
                    
                    BoxLayout: 
                        orientation: 'vertical'
    
                        ScrollView:
                            MDList:
                                id: pathUploadFileList
                    
                  


            PageAllFile:
                name: "PageAllFile"
                id: PageAllFileScreen

                MDBoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                       
                        title: "Все файлы"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    MDBoxLayout: 
                        orientation: 'vertical'
    
                        ScrollView:
                            MDList:
                                id: containerAllFileList
                    

                           

            


            PageResult:
                name: "PageResult"
                id: PageResult

                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint: (1, 1)

                    MDTopAppBar:
                        
                        title: "Результат"
                        elevation: 0
                        left_action_items: [["arrow-left", lambda x: app.result_page_exit_callbak()]]
                        right_action_items:
                            [['export', lambda x: app.exportFile(), "Экспорт в xls"]]
                
                    BoxLayout:
                        id: boxResult
                        orientation: "vertical"
                        size_hint: 1, 0.9
            

            PageExportExcel:
                name: "PageExport"
                id: PageExport
                
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint: (1, 1)

                    MDTopAppBar:
                        
                        title: "Экспорт"
                        elevation: 0
                        left_action_items: [["arrow-left", lambda x: app.result_page_exit_callbak()]]
                    

                    BoxLayout:
                        orientation: "vertical"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                spacing: '8dp'
                padding: '8dp'
                orientation: "vertical"
                
                MDLabel: 
                    text: "Меню"
                    size_hint_y: None

                Button:
                    text: "Загрузить файлы"
                    size_hint: 0.9, 0.05
                    on_release: manager.current='PageUploadFile'
                
                Button:
                    text: "Все файлы"
                    size_hint: 0.9, 0.05
                    on_release: app.openPageAllFile()
                    on_release: manager.current='PageAllFile'
                
                ScrollView:
"""



Window.size = (720, 1024)


class ScreenManagement(ScreenManager):
    pass


# pages (screen)
class PageUploadFile(Screen):
    pass
    
class PageAllFile(Screen):
    pass

class PageResult(Screen):
    pass

class PageExportExcel(Screen):
    pass




# sidebar content
class ContentNavigationDrawer(MDBoxLayout):
    pass


    
    
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
        self.errorFile=[] 
        self.db = USE_DB()
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            selector='multi'
        )

    def build(self):
        return Builder.load_string(ui)
       

    # Файл менеджер

    def file_manager_open(self):
        self.arrayExport = []
        self.errorFile = []
        self.arrayPath = []
        self.file_manager.show('/')  
        self.manager_open = True

    def select_path(self, path):
        self.arrayPath = path
        self.manager_open = False
        self.file_manager.close()
        self.afterExitManagerFile()
       
       
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
        
    
    
         
    def afterExitManagerFile(self):
        for i in range(len(self.arrayPath)):
            self.file_name = self.arrayPath[i].split('/')[len(self.arrayPath[i].split('/'))-1]
            if (self.file_name.split('.')[len(self.file_name.split('.'))-1]) != "pdf":
                self.status = f"[color=ff0000]Данный формат {(self.file_name.split('.')[len(self.file_name.split('.'))-1])} не поддерживается"
                self.errorFile.append(self.arrayPath[i])
            else:
                self.status = f'Файл загружен'
            self.root.ids.pathUploadFileList.add_widget(
                ThreeLineListItem(text=f"Название фала: {self.file_name}", secondary_text=f"Путь к файлу: {self.arrayPath[i]}", tertiary_text=f"Статус: {self.status}")
            )

        self.edit_arrayPath_of_error()


    #Database 

    def useDbInAllFilePage(self):
        resultData = self.db.getAllFilesWithResults()
        return resultData

    def saveFileInDb(self):
        files = []
        db2 = USE_DB()
        p = GPZU_parser(files_paths=self.arrayPath)
        data = p.parse()
    
        
        for file_path,_ in data.items():
            for name,result in data[file_path].items():
                file = File(file_path,name,result)
                files.append(file)
        
        db2.insertElementFile(files)

    # Subprocces after load pages and callbacks
    def callbackOpenPageExport(self):
        self.root.ids.manager.current = 'PageExport'


    def edit_arrayPath_of_error(self):
        for i in range(len(self.errorFile)):
            self.arrayPath.remove(self.errorFile[i])
        self.saveFileInDb()

    def callbackPressOnAllFileItem(self, instance):
        self.openPageResult(self.getTableToResultOnPressItemALLFile(instance.id))
        self.root.ids.manager.current = 'PageResult'
        data = self.db.getOneFileById(instance.id)
        self.arrayExport = [data.path]

    def result_page_exit_callbak(self, name_page = 'PageAllFile'):
        self.openPageAllFile()
        self.root.ids.manager.current = name_page

    def openPageResultAfterUpload(self):
        self.openPageResult(self.getTableToResultAfterUpload())
        self.root.ids.manager.current = 'PageResult'
        self.arrayExport = self.arrayPath
    
    def openPageAllFile(self):
        self.root.ids.containerAllFileList.clear_widgets()
        files = self.useDbInAllFilePage()
        for file in files:
            id = str(file.id)
            self.root.ids.containerAllFileList.add_widget(
                ThreeLineListItem(
                    id=id,
                    text=f"Название фала: {file.name}", 
                    secondary_text=f"Путь к файлу: {file.path}", 
                    tertiary_text=f"Дата: {file.date}", 
                    on_release=self.callbackPressOnAllFileItem,
                    )
            )




    # Create tables result
    def getTableToResultAfterUpload(self):
        listColumn = []
        rowData = []
        arrayLocalFileID = []
        data = self.db.getAllFilesWithResults()
        for file in data: 
            for i in range(len(self.arrayPath)):
                if(self.arrayPath[i] == file.path):
                    arrayLocalFileID.append(file.id)
        
        for i in range(len(arrayLocalFileID)):
            data = self.db.getOneFileById(arrayLocalFileID[i])
            dataKeys = data.result.keys()
            nameColumn = list(dataKeys)
            if len(listColumn) == 0:
                for j in range(len(nameColumn)):
                    if j == 6:
                        listColumn.append((nameColumn[j], dp(150)))
                    else:
                        listColumn.append((nameColumn[j], dp(90)))

            row = []
            for g in range(len(nameColumn)):
                row.append(data.result.get(nameColumn[g]))
            rowData.append(tuple(row))
        
        data_tables = MDDataTable(
            rows_num=10,
            use_pagination=True,
            column_data=listColumn,
            row_data=rowData,
            # sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        return data_tables
            
    def getTableToResultOnPressItemALLFile(self, id):
        data = self.db.getOneFileById(id)
        listColumn = []
        rowData = []
        dataKeys = data.result.keys()
        nameColumn = list(dataKeys)
        if len(listColumn) == 0:
                for j in range(len(nameColumn)):
                    listColumn.append((nameColumn[j], dp(80)))
        row = []
        for g in range(len(nameColumn)):
            row.append(data.result.get(nameColumn[g]))
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
 




    def openPageResult(self, data_table):
        self.root.ids.boxResult.clear_widgets()
        base = FloatLayout(
            size_hint = (1, 1)
        )  
        box = MyBox()
        box.add_widget(Widget(size_hint_y=0))
        box.add_widget(Widget(size_hint_y=0))
        box.add_widget(data_table)
        scroll = ScrollView(do_scroll_y=False, pos_hint={"center_y": .5})
        scroll.add_widget(box)
        base.add_widget(scroll)
        self.root.ids.boxResult.add_widget(base)
 

    def exportFile(self):
        exp = GPZU_parser(files_paths=self.arrayExport)
        exp.parse()
        folder_path = filechooser.choose_dir()
        exp.to_excel(str(folder_path[0]), "file_"+str(uuid.uuid4()))
        self.arrayExport = []
      

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back(on_selection=self.handle_selection)
        return True
    

MyApp().run()