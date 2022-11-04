import sqlite3
from datetime import *

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

def createDBTableFiles():
    try:
        res = cur.execute("CREATE TABLE files (id text not null primary key, path text, name text, date text)")
        return True
    except:
        return False

def createDBTableResult():
    try:
        res = cur.execute("""CREATE TABLE result (
            resultid not null text,
            fileid text,
            ...
            unique number text                            #Уникальный номер
            number_of_gpzu text                           #номер ГПЗУ
            date_issuance_gpzu                            #Дата выдачи ГПЗУ
            status_gpzu text                              #Статус ГПЗУ
            period_validity_gpzu text                     #Срок действия ГПЗУ
            owner_other_recipient_gpzu text               #Правообладатель или иной получатель ГПЗУ
            type_owner_recipient_gpzu text                #Тип правообладателя или получателя ГПЗУ
            administrative_district text                  #Административный округ
            district_settlement text                      #Район (поселение)
            construction_address text                     #Строительный адрес
            cadastral_number_land_plot                    #Кадастровый номер земельного участка (ЗУ)
            availability_territory_planning_project text  #Наличие проекта планировки территории (ППТ)
            details_document text                          #Реквизиты документа ППT
            availability_separate_project_land_gpzu text   #Наличие отдельного проекта межевания территории в границах ГПЗУ 
            details_document_project_land_survey text      #Реквизиты документа проекта межевания
            name_conditional_use_group text                #Наименование условной группы использования
            codes_main_types_permitted_uses text           #Коды основных видов разрешенного использования (ВРИ)
            area_land_plot_area text                       #Площадь земельногоучастка (ЗУ), кв.м
            availability_sub_zones_land text               #Наличие подзон ЗУ, номера
            areas_subzones text                            #Площади подзон ЗУ,  кв.м
            building_height text                           #Высота застройки
            number_floors text                             #Количество этажей
            percentage_builtup_area text                   #Процент застроенности
            building_density text                          #Плотность застройки
            purpose_ocs text                               #Назначение ОКС
            Name_description_ocs text                      #Наименование, описание ОКС
            presence_objects_planning_regulations_not apply text  #Наличие объектов на которые действие градостроительного регламента не распространяется или не устанавливаеться
            floor_area_total text                          #Всего
            floor_area_total_residential_development text  #Жилой застройки
            floor_area_total_nonresidential_development text  #Нежилой застройки
            floor_area_total_living_quarters text          #Жилых помещений
            built_in_attached_freestanding_non_residential_premises
            ...
            FOREIGN KEY(fileid) REFERENCES files(artistid)
            )""")
        return True
    except:
        return False


def CreateElementDBFiles(files):
    for i in range(len(files)):
        cur.execute("insert into files values(" + str(files[i].id) +")")


def SelectFileList():
    for row in cur.execute("SELECT * FROM files"):
        print(row)
    

CreateElementDBFiles([{"id": "1", "path": "/user1", "name": "212", "date": "123123"}, {"id": "2", "path": "/user2", "name": "212123", "date": "444123123"}])
    
SelectFileList()