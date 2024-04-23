from pymongo import MongoClient
from database.dataclass.school import School
import certifi


class DatabaseHelper:

    def __init__(self):
        ca = certifi.where()
        self.client = MongoClient('mongodb+srv://kamc:kamc123456qwer!@kamc.q7fcfov.mongodb.net/', tlsCAFile=ca)

    def get_all_data_from_school_name(self):
        school_dict_list = self._get_all_data_kamc()
        school_list = []
        for school_dict in school_dict_list:
            school = School()
            for k, v in school_dict.items():
                setattr(school, k, v)
            school_list.append(school)
        return school_list

    def _get_all_data_kamc(self):
        db = self.client['kamc']
        return [doc for doc in db['school'].find()]

    def _get_all_value_by_key_kamc(self, key, year=None, school=None):
        db = self.client['kamc']
        proj = {'대학명': 1, key: 1, '연도': 1}
        if school is not None and year is not None:
            return [doc for doc in db['school'].find({"대학명": school, "연도": year}, proj)]
        if school is not None:
            return [doc for doc in db['school'].find({"대학명": school}, proj)]
        if year is not None:
            return [doc for doc in db['school'].find({"연도": year}, proj)]
        return [doc for doc in db['school'].find({}, proj)]

    def _get_data_from_school_name(self, school_name):
        db = self.client['kamc']
        school_dict_list = [doc for doc in db['school'].find({"대학명": school_name})]
        school_list = []
        for school_dict in school_dict_list:
            school = School()
            for k, v in school_dict.items():
                setattr(school, k, v)
            school_list.append(school)
        return school_list

    def update_school_data(self, school):
        db = self.client['kamc']
        collection = db['school']
        uid = getattr(school, '_id', None)

        set_dict = {}
        for attr_name in [d for d in dir(school) if not d.startswith('__')]:
            set_dict[attr_name] = getattr(school, attr_name)
        if uid is None:
            collection.insert_one(set_dict)
        else:
            collection.update_one({'_id': uid}, {'$set': set_dict}, upsert=True)


database_helper = DatabaseHelper()
school_list = database_helper.get_all_data_from_school_name()
