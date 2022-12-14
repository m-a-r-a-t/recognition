from typing import List, Optional
import uuid
import sqlite3
import json


class File:
    def __init__(self, path, name,  result, id=0,  date='',):
        self.id = id
        self.path = path
        self.name = name
        self.date = date

        self.result = result


class USE_DB:
    def __init__(self):
        self.__conn = sqlite3.connect("db.sqlite3")
        self.__conn.row_factory = sqlite3.Row
        self.__createTableFile()

    def __createTableFile(self):
        cur = self.__conn.cursor()
        try:
            res = cur.execute("""CREATE TABLE files (
                id INTEGER NOT NULL UNIQUE  PRIMARY KEY,
                path TEXT NOT NULL,
                name TEXT NOT NULL,
                date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                data TEXT NOT NULL
                )""")

            print('Table files created')
        except Exception as e:
            print("[INFO]", e)

    def insertElementFile(self, files: List[File]):
        ids = []
        cur = self.__conn.cursor()
        cur.execute("begin")
        try:
            for file in files:
                cur.execute("INSERT INTO files (path,name,data) VALUES(?,?,?)", (file.path, file.name, json.dumps(file.result)))
                ids.append(cur.lastrowid)
            cur.execute("commit")
        except Exception as e:
            cur.execute("rollback")
            print("Transaction failed", e)
        finally:
            cur.close()

        return ids

    def getAllFilesWithResults(self,):
        cur = self.__conn.cursor()
        cur.execute("SELECT * FROM files")
        data = [dict(row) for row in cur.fetchall()]
        return [File(path=d["path"], name=d["name"], result=json.loads(d["data"]), id=d["id"], date=d["date"]) for d in data]

    def getOneFileById(self, idd: int):
        cur = self.__conn.cursor()
        cur.execute("SELECT * FROM files WHERE id=?", (idd,))
        data = dict(cur.fetchone())
        return File(path=data["path"], name=data["name"], result=json.loads(data["data"]), id=data["id"], date=data["date"])

    def getFilesByIds(self, ids: List[int]):
        cur = self.__conn.cursor()
        cur.execute(f"SELECT * FROM files WHERE id in ({','.join(['?'] * len(ids))})", ids)

        data = [dict(row) for row in cur.fetchall()]
        return [File(path=d["path"], name=d["name"], result=json.loads(d["data"]), id=d["id"], date=d["date"]) for d in data]


# if __name__ == "__main__":
#     db = USE_DB()

#     data = db.getAllFilesWithResults();
#     for file in data:
#         print('========================================================')
#         print(file.id)
#         print(file.path)
#         print(file.date)
#         print(file.name)
#         print(file.result)

    # p = GPZU_parser(files_paths=['test/parser/RU77101000-040954-GPZU.pdf'])

    # data = p.parse()

    # arrayKeys = data.keys()
    # x = data.get(list(arrayKeys)[0])
    # print(x)

    # result = x

    # file = File('/Users/egormuhaev/Desktop/app-pithon/test/parser/RU77101000-040954-GPZU.pdf', result,)
    # print(db.insertElementFile([file]))  # c?????? ?????? ???????????????? ???????????? ????????????
    # data = db.getAllFilesWithResults()
    # # file
    # for file in data:
    #     print('========================================================')
    #     print(file.id)
    #     print(file.path)
    #     print(file.date)
    #     print(file.name)
    #     print(file.result)

    # one_row = db.getOneFileById(1)  # ?????????????????? ?????????? ????????

    # print(one_row)
