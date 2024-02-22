import pymongo
from pymongo import MongoClient
from pandas import DataFrame
import plotly.express as px
from database.dataclass.school import School
from util import total_state_key_dict
import pymysql


class DatabaseHelper:

    def __init__(self):
        self.client = MongoClient('mongodb://kamc_root:kamc123456qwer!@43.201.146.205:19999/?authMechanism=DEFAULT')

    def get_all_data_from_school_name(self):
        school_dict_list = self._get_all_data_kamc()
        school_list = []
        for school_dict in school_dict_list:
            school = School()
            for k, v in school_dict.items():
                setattr(school, k, v)
            school_list.append(school)
        return school_list

    def get_professor_info(self, school_list):
        db = self.client[f'KAMC_EDU_교수']
        for school in school_list:
            department_information_list = []
            for year in range(2018, 2021):
                collection = db[f"{year}_교원수_기초의학(전체)"]
                data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    department_information_list.append(data)
                collection = db[f"{year}_교원수_임상의학(소속교실별)"]
                data_list2 = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list2:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    department_information_list.append(data)

                collection = db[f"{year}_교원수_임상의학(전체)"]
                data_list3 = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list3:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    department_information_list.append(data)
                collection = db[f"{year}_교원수_전체"]
                data_list4 = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list4:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    department_information_list.append(data)
            school['교원수'] = department_information_list

        for school in school_list:
            tmp = []
            for year in range(2018, 2021):
                collection = db[f'{year}_의학교육 관련 연수']
                data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    tmp.append(data)
            school['의학교육 관련 연수'] = tmp
        for school in school_list:
            tmp = []
            for year in range(2018, 2021):
                collection = db[f'{year}_전임교원 수 변화']
                data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    tmp.append(data)
                school['전임교원 수 변화'] = tmp
        return school_list

    def get_curriculum_info(self, school_list):
        db = self.client[f'KAMC_EDU_교육과정']
        col_list = set(['_'.join(name.split('_')[1:]) for name in db.list_collection_names()])
        for school in school_list:
            for col_name in col_list:
                tmp = []
                for year in range(2018, 2021):
                    collection = db[f'{year}_{col_name}']
                    data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                    for data in data_list:
                        data.pop('_id')
                        data.pop('대학명')
                        key_list = list(data.keys())
                        for k in key_list:
                            v = data[k]
                            if v != v:
                                data[k] = None
                        data['year'] = year
                        tmp.append(data)
                    school[col_name] = tmp
        return school_list

    def get_facility_info(self, school_list):
        db = self.client[f'KAMC_EDU_시설']
        col_list = set(['_'.join(name.split('_')[1:]) for name in db.list_collection_names()])
        for school in school_list:
            for col_name in col_list:
                tmp = []
                for year in range(2018, 2021):
                    collection = db[f'{year}_{col_name}']
                    data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                    for data in data_list:
                        data.pop('_id')
                        data.pop('대학명')
                        key_list = list(data.keys())
                        for k in key_list:
                            v = data[k]
                            if v != v:
                                data[k] = None
                        data['year'] = year
                        tmp.append(data)
                    school[col_name] = tmp
        return school_list

    def get_school_info(self, school_list):
        for school in school_list:
            db = self.client[f'KAMC_EDU_group']
            collection = db[f'group']
            data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
            for data in data_list:
                data.pop('_id')
                data.pop('대학명')
                key_list = list(data.keys())
                for k in key_list:
                    v = data[k]
                    if v != v:
                        data[k] = None
                school.update(data)
        for school in school_list:
            db = self.client[f'KAMC_Comment']
            collection = db[f'user']
            data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
            for data in data_list:
                data.pop('_id')
                data.pop('대학명')
                key_list = list(data.keys())
                for k in key_list:
                    v = data[k]
                    if v != v:
                        data[k] = None
                school.update(data)
        return school_list

    def get_general_info(self, school_list):
        for school in school_list:
            db = self.client[f'KAMC_EDU_일반현황']
            col_name = '대학기본정보'
            tmp = []
            for year in range(2018, 2021):
                collection = db[f'{year}_{col_name}']
                data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                for data in data_list:
                    data.pop('_id')
                    data.pop('대학명')
                    key_list = list(data.keys())
                    for k in key_list:
                        v = data[k]
                        if v != v:
                            data[k] = None
                    data['year'] = year
                    tmp.append(data)
                school[col_name] = tmp
        return school_list

    def get_student_info(self, school_list):
        db = self.client[f'KAMC_EDU_학생']
        col_list = set(['_'.join(name.split('_')[1:]) for name in db.list_collection_names()])
        for school in school_list:
            for col_name in col_list:
                tmp = []
                for year in range(2018, 2021):
                    collection = db[f'{year}_{col_name}']
                    data_list = [doc for doc in collection.find({"대학명": school['대학명']})]
                    for data in data_list:
                        data.pop('_id')
                        data.pop('대학명')
                        key_list = list(data.keys())
                        for k in key_list:
                            v = data[k]
                            if v != v:
                                data[k] = None
                        data['year'] = year
                        tmp.append(data)
                    school[col_name] = tmp
        return school_list

    def _get_all_data_from_school_name(self):
        db = self.client[f'KAMC_Comment']
        collection = db[f'numbering']
        data_list = [doc for doc in collection.find()]
        school_list = [{"대학명": data['대학명'], "입학정원": data['입학정원']} for data in data_list]
        school_list = self.get_school_info(school_list)
        school_list = self.get_professor_info(school_list)
        school_list = self.get_curriculum_info(school_list)
        school_list = self.get_facility_info(school_list)
        school_list = self.get_general_info(school_list)
        school_list = self.get_student_info(school_list)
        return school_list

    def _get_all_data_kamc(self):
        db = self.client['kamc']
        return [doc for doc in db['school'].find()]

    def update_school_data(self, school):
        db = self.client['kamc']
        collection = db['school']
        uid = getattr(school, '_id')

        set_dict = {}
        for attr_name in [d for d in dir(school) if not d.startswith('__')]:
            set_dict[attr_name] = getattr(school, attr_name)

        # upsert
        collection.update_one({'_id': uid}, {'$set': set_dict}, upsert=True)


database_helper = DatabaseHelper()
school_list = database_helper.get_all_data_from_school_name()
