from typing import List
from gpzu_parser.gpzu_parser import GPZU_parser
import pandas as pd
from model import USE_DB, File
from tkinter import Tk, filedialog
import os

class Gpzu_Service:
    def __init__(self) -> None:
        pass

    def calc_and_save_gpzus(self, paths: List[str]):
        files = []
        p = GPZU_parser(files_paths=paths)
        data = p.parse()

        for file_path, _ in data.items():
            for name, result in data[file_path].items():
                file = File(file_path, name, result)
                files.append(file)

        try:
            return USE_DB().insertElementFile(files)
        except Exception as e:
            raise e

    def get_all_gpzus(self,):
        result = USE_DB().getAllFilesWithResults()
        return result

    def export_to_excel(self, ids: List[int]):
        data = USE_DB().getFilesByIds(ids)

        if len(data) != 0:
            new_data = [file.result for file in data]
            df = pd.DataFrame.from_records(new_data)
            # df = pd.DataFrame.from_dict(self.results, orient='index').iloc[:, 10:]
            df = df.dropna()
            # df.insert(0, 'Уникальный номер записи', '')
            # df['Уникальный номер записи'] = df.index
            # df.index = np.arange(1, len(df) + 1)
            root = Tk()
            root.attributes("-topmost", True)
            root.withdraw()
            file_path_to_save = filedialog.asksaveasfilename(parent=root,filetypes=[('Excel', '.xlsx')])
            if os.name == 'nt':
                file_path_to_save += '.xlsx'
            print(os.name,file_path_to_save)
            if file_path_to_save == "":
                return
            # print(file_path_to_save)
            df.to_excel(file_path_to_save)
