from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp


Builder.load_string("""
<MyWidget>:
    background_color: 0, 0, 0, 1
    id: my_widget
    FileChooserListView:
        id: filechooser
        on_selection: app.selected(filechooser.selection)
    MDList:
        id: pathUploadFileList

""")


class MyWidget(BoxLayout):
    pass


class MyApp(MDApp):
    def build(self):
        return MyWidget()
    
    def selected(self,filename):
        self.root.ids.pathUploadFileList.add_widget(
                OneLineListItem(text=f"File: {filename[0]}")
            )


if __name__ == '__main__':
    MyApp().run()
