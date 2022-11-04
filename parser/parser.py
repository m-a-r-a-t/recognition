from typing import List
import numpy as np
import pandas as pd
import fitz  # pip install PyMuPDF
import datetime
import os
import re


class GPZU_parser:
    def __init__(self, files_paths: List[str]) -> None:
        self.files_paths = files_paths
        self.results = {}

    def __get_empty_set(self,):
        this = {
            '№ п/п': '',
            'Уникальный номер записи': '',
            'Номер ГПЗУ': '',
            'Дата выдачи ГПЗУ': '',
            'Статус ГПЗУ': '',
            'Срок действия ГПЗУ': '',
            'Правообладатель или иной получатель ГПЗУ': '',
            'Тип правообладателя или получателя ГПЗУ': '',

            'Административный округ': '',
            'Район (поселение)': '',
            'Строительный адрес': '',
            'Кадастровый номер земельного участка (ЗУ)': '',
            'Наличие проекта планировки территории (ППТ) в границах ГПЗУ': '',
            'Реквизиты документа ППТ': '',
            'Наличие отдельного проекта межевания территории в границах ГПЗУ': '',
            'Реквизиты документа проекта межевания': '',

            'Наименование условной группы использования ЗУ по ВРИ': '',
            'Коды основных видов разрешенного использования (ВРИ) земельного  участка (ЗУ)': '',

            'Площадь земельного  участка (ЗУ), кв.м': '',
            'Наличие подзон ЗУ, номера': '',
            'Площади подзон ЗУ, кв.м': '',

            'Высота застройки, м': '',
            'Количество этажей, шт': '',
            'Процент застроенности, %': '',
            'Плотность застройки, тыс. кв. м/га': '',

            'Назначение ОКС': '',
            'Наименование, описание ОКС': '',
            'Наличие объектов на которые действие градостроительного регламента не распространяется или не устанавливаеться': '',

            '28': '',
            '29': '',
            '30': '',
            '31': '',
            '32': '',
            '33': '',
            '34': '',
            '35': '',
            '36': '',
            '37': '',
            '38': '',
            '39': '',
            '40': '',
            '41': '',
            '42': '',
            '43': '',
            '44': '',
            '45': '',
            '46': '',
            '47': '',
            '48': '',
            '49': '',
            '50': '',
            '51': '',
            '52': '',
            '53': '',
            '54': '',
            '55': '',
            '56': '',
            '57': '',
            '58': '',
            '59': '',
            '60': '',
            '61': '',
            '62': ''
        }
        return this

    def __parse_number(self, text):
        for key, item in enumerate(text):

            if item.find('RU') >= 0 or item.find('РФ-') >= 0:
                return item.replace('№ ', '')

        return False

    def __parse_count(self, text):
        zu_names = []
        zu_keys = []
        for key, item in enumerate(text):
            # земельные участки
            if item.find('чертеже ГПЗУ') >= 0:
                podzona = ''.join(item.split(' ')[0:2])
                zu_names.append(podzona)
                zu_keys.append(key)

        return zu_names, zu_keys

    def __parse_pdf(self, text, zu_names=[], zu_keys=[], zu_name=''):

        this = self.__get_empty_set()
        trash = {}

        for key, item in enumerate(text):

            if item.find('RU') >= 0 or item.find('РФ-') >= 0:
                this['Номер ГПЗУ'] = item

            if item.find('ата выдачи') >= 0:
                this['Дата выдачи ГПЗУ'] = item.replace('Дата выдачи ', '')

            if item.find('Срок действия') >= 0:
                srok = item.split('по ')
                if (len(srok) > 1):
                    this['Срок действия ГПЗУ'] = srok[-1]

            if item.find('участка подготовлен на основании') >= 0:
                trash['_подготовлен'] = key

            if item.find('стонахождение земельного') >= 0:
                trash['_местонахождение'] = key

            if item.find('в единый государственный реестр объектов культурного') >= 0:
                trash['_культурного'] = key

            if item.find('исание границ') >= 0:
                trash['_описание'] = key

            if item.find('щадь земельного участка') >= 0:
                trash['_площадь'] = key

        if trash['_местонахождение'] and trash['_описание']:
            this['местонахождение'] = " ".join(text[(trash['_местонахождение']+1):trash['_описание']])

        if trash['_подготовлен'] and trash['_местонахождение']:
            this['Правообладатель или иной получатель ГПЗУ'] = " ".join(text[(trash['_подготовлен']+1):trash['_местонахождение']]).replace('обращения ', '').split(' от ')[0]
            if len(re.findall('акционер|фонд|бщест', this['Правообладатель или иной получатель ГПЗУ'])) > 0:
                this['Тип правообладателя или получателя ГПЗУ'] = 'ЮЛ'
            else:
                this['Тип правообладателя или получателя ГПЗУ'] = 'ФЛ или ИП'

        if trash['_площадь']:
            q = text[(trash['_площадь'])]+text[(trash['_площадь']+1)]+text[(trash['_площадь']+2)]
            q = ''.join(i for i in q if not i.isalpha())
            this['Площадь земельного  участка (ЗУ), кв.м'] = q.split('±')[0].replace(' ,       ,  – ', '')\
                .replace('  -    :  ,    , ', '').replace('  : ', '').replace(' .          ', '')

        if this['Срок действия ГПЗУ']:
            try:
                now_date = datetime.datetime.strptime(this['Срок действия ГПЗУ'], '%d.%m.%Y')
            except ValueError:
                now_date = datetime.datetime.strptime(this['Срок действия ГПЗУ'], '%Y-%m-%d')
            if now_date > datetime.datetime.now():
                this['Статус ГПЗУ'] = 'Действует'
            else:
                this['Статус ГПЗУ'] = 'Не действует'

        # Земельные участки
        if len(zu_names) > 0 and len(zu_name) > 1:
            zu_index = zu_names.index(zu_name)
            if zu_keys[zu_index] == max(zu_keys):
                find_next = trash['_культурного']
            else:
                find_next = zu_keys[zu_index+1:][0]
            trash['zu'] = "".join(text[zu_keys[zu_index]+1:find_next])

            try:
                this['Строительный адрес'] = trash['zu'].split('Адрес:')[1].split(' Назначение:')[0]
            except IndexError:
                pass
            try:
                this['Строительный адрес'] = trash['zu'].split('Адрес:')[1].split(' Назначение:')[0]
            except IndexError:
                pass
            try:
                this['Наличие подзон ЗУ, номера'] = zu_name
            except IndexError:
                pass
            try:
                this['Площади подзон ЗУ, кв.м'] = float(trash['zu'].split('Площадь: ')[1].split(' кв.м')[0]
                                                        .replace(' ', '').replace(',', '.'))
            except IndexError:
                pass
            try:
                this['Кадастровый номер земельного участка (ЗУ)'] = trash['zu'].split('Кадастровый номер: ')[1].split(';')[0]
            except IndexError:
                pass
            try:
                this['Наименование условной группы использования ЗУ по ВРИ'] = trash['zu'].split('Назначение: ')[1].split(';')[0]
            except IndexError:
                pass
            try:
                this['Количество этажей, шт'] = trash['zu'].split('Количество этажей: ')[1].split(';')[0]
            except IndexError:
                pass
            try:
                this['Высота застройки, м'] = trash['zu'].split('Количество этажей: ')[1].split(';')[0]
            except IndexError:
                pass

        return this
    # pd.DataFrame(this, index=[doc.name])

    def parse(self) -> dict:
        i = 0
        # self.results = {}
        for p in self.files_paths:
            with fitz.open(p) as doc:
                text = ""
                html = ""
                for page in doc:
                    text += page.get_text()
                text = text.split('\n')

                now_number = self.__parse_number(text)

                if now_number:
                    zu_names, zu_keys = self.__parse_count(text)
                    if len(zu_names) > 0:
                        for zu_name in zu_names:
                            i += 1
                            self.results[now_number+zu_name] = self.__parse_pdf(text, zu_names, zu_keys, zu_name=zu_name)
                        else:
                            i += 1
                            self.results[now_number] = self.__parse_pdf(text)
                        self.results[now_number]['№ п/п'] = i

        return self.results

    def to_excel(self, folder_path: str, file_name: str):
        df = pd.DataFrame.from_dict(self.results, orient='index').iloc[:, 10:]
        df = df.dropna()
        df.insert(0, 'Уникальный номер записи', '')
        df['Уникальный номер записи'] = df.index
        df.index = np.arange(1, len(df) + 1)

        df.to_excel(folder_path+'/'+file_name+".xlsx")
