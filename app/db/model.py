from db.use_db import *
import uuid
import sqlite3
from test.parser.parser import GPZU_parser



class Result:
    def __init__(self, fileId, filePath):
        self.result_id = uuid.uuid4()
        self.file_id = fileId
        self.result_data = self.dataResultConvert(filePath)
        pass

    def dataResultConvert(self, filePath):
        p = GPZU_parser(files_paths=[filePath])
        data = p.parse()
        return data.get(list(data.keys())[0])


class File:
    def __init__(self, path):
        self.path = path
        self.file_name = self.path.split('/')[len(self.path.split('/'))-1]
        self.id = uuid.uuid4()


class USE_DB:
    def __init__(self, filePath, Result):
        self.file = File(filePath)
        self.Result = Result(self.file.id, self.file.path)
        pass 

    def CreateTableFile(self):
            pass
    
    def CreateTableResult(self):
        pass

    
    def InsertElementFile(self):
        #insertFiletable
        #insertResult
        pass



#Эти методы вне класса

def SelectInFileAll():
    pass

def SelectInResultById():
    pass