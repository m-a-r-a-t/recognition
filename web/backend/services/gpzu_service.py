from typing import List
from gpzu_parser.gpzu_parser import GPZU_parser

from web.backend.model import USE_DB, File


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
