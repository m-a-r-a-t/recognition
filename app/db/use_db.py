import sqlite3
from datetime import *

conn = sqlite3.connect("db.sqlite3")
conn.row_factory = sqlite3.Row


def createFilesTable(conn):
    cur = conn.cursor()
    try:
        res = cur.execute("""CREATE TABLE files (
            id INTEGER NOT NULL UNIQUE  PRIMARY KEY,
            path TEXT NOT NULL,
            name TEXT NOT NULL,
            date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""")
        return True
    except Exception as e:
        # print(e)
        return False


def createResultTable(conn):
    cur = conn.cursor()
    try:
        res = cur.execute("""CREATE TABLE result (
            resultid TEXT NOT NULL,
            fileid TEXT NOT NULL UNIQUE,
            nn_number TEXT 
            unique_number TEXT,                            '''Уникальный номер'''
            number_of_gpzu TEXT,                           '''номер ГПЗУ'''
            date_issuance_gpzu TEXT,                            '''Дата выдачи ГПЗУ'''
            status_gpzu TEXT ,                             '''Статус ГПЗУ'''
            period_validity_gpzu TEXT,                  '''Срок действия ГПЗУ'''
            owner_other_recipient_gpzu TEXT,            '''Правообладатель или иной получатель ГПЗУ'''
            type_owner_recipient_gpzu TEXT,            '''Тип правообладателя или получателя ГПЗУ'''
            administrative_district TEXT,                 '''Административный округ'''
            district_settlement TEXT,                   '''Район (поселение)'''
            construction_address TEXT,                  '''Строительный адрес'''
            cadastral_number_land_plot TEXT,                 '''Кадастровый номер земельного участка (ЗУ)'''
            availability_territory_planning_project TEXT, '''Наличие проекта планировки территории (ППТ)'''
            details_document TEXT,                          '''Реквизиты документа ППT'''
            availability_separate_project_land_gpzu TEXT,   '''Наличие отдельного проекта межевания территории в границах ГПЗУ''' 
            details_document_project_land_survey TEXT,      '''Реквизиты документа проекта межевания'''
            name_conditional_use_group TEXT,                '''Наименование условной группы использования'''
            codes_main_types_permitted_uses TEXT,           '''Коды основных видов разрешенного использования (ВРИ)'''
            area_land_plot_area TEXT,                      '''Площадь земельногоучастка (ЗУ), кв.м'''
            availability_sub_zones_land TEXT,              '''Наличие подзон ЗУ, номера'''
            areas_subzones TEXT,                       '''Площади подзон ЗУ,  кв.м'''
            building_height TEXT,                           '''Высота застройки'''
            number_floors TEXT,                             '''Количество этажей'''
            percentage_builtup_area TEXT,                  '''Процент застроенности'''
            building_density TEXT,                          '''Плотность застройки'''
            purpose_ocs TEXT,                               '''Назначение ОКС'''
            Name_description_ocs TEXT,                      '''Наименование, описание ОКС'''
            presence_objects_planning_regulations_not apply TEXT,  '''Наличие объектов на которые действие градостроительного регламента не распространяется или не устанавливаеться'''
            28 TEXT
            29 TEXT
            30 TEXT 
            31 TEXT
            32 TEXT
            33 TEXT
            34 TEXT
            35 TEXT
            36 TEXT
            37 TEXT
            38 TEXT
            39 TEXT
            40 TEXT
            41 TEXT
            42 TEXT
            43 TEXT
            44 TEXT
            45 TEXT
            46 TEXT
            47 TEXT
            48 TEXT
            49 TEXT 
            50 TEXT
            51 TEXT
            52 TEXT
            53 TEXT
            54 TEXT
            55 TEXT
            56 TEXT
            57 TEXT
            58 TEXT
            59 TEXT
            60 TEXT
            61 TEXT
            62 TEXT
            FOREIGN KEY(fileid) REFERENCES files(id) ON DELETE CASCADE
            )""")
        return True
    except Exception as e:
        # print(e)
        return False


def insertFiles(cur, files):
    for file in files:
        cur.execute("INSERT INTO files (path,name) VALUES(?,?)", (file["path"], file["name"]))


def getAllFiles(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM files")
    return [dict(row) for row in cur.fetchall()]


def getAllResults(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM result")
    return [dict(row) for row in cur.fetchall()]


createFilesTable(conn)
createResultTable(conn)

cur = conn.cursor()
cur.execute("begin")
try:
    insertFiles(cur, [{"path": "/user1", "name": "212", }, {"path": "/user2", "name": "212123", }])
    cur.execute("commit")
except Exception as e:
    cur.execute("rollback")
    print("Transaction failed", e)

cur.close()

files = getAllFiles(conn)
results = getAllResults(conn)

print("Files", files)
print("Results", results)
