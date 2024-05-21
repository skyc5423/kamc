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

    def _get_data_from_school_name_year(self, school_name=None, year=None):
        if school_name is None and year is None:
            return self._get_all_data_kamc()
        db = self.client['kamc']
        if school_name is not None and year is not None:
            school_dict_list = [doc for doc in db['school'].find({"대학명": school_name, "연도": year})]
        elif school_name is not None:
            school_dict_list = [doc for doc in db['school'].find({"대학명": school_name})]
        else:
            school_dict_list = [doc for doc in db['school'].find({"연도": year})]
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

    def get_notice(self):
        db = self.client['kamc']
        return [doc for doc in db['notices'].find({'active': True})]

    def insert_notice(self, notice):
        try:
            db = self.client['kamc']
            collection = db['notices']
            collection.insert_one(notice)
            return True
        except:
            return False

    def deactivate_notice(self, notice):
        try:
            db = self.client['kamc']
            collection = db['notices']
            collection.update_one({'_id': notice['_id']}, {'$set': {'active': False}})
            return True
        except:
            return False

    def verify_login(self, user_id, pw):
        try:
            db = self.client['kamc']
            collection = db['users']
            user = collection.find_one({'id': user_id, 'password': pw})
            return user
        except:
            return None

    def get_all_user(self):
        db = self.client['kamc']
        return [doc for doc in db['users'].find()]

    def add_user(self, user):
        try:
            db = self.client['kamc']
            collection = db['users']
            collection.insert_one(user)
            return True
        except:
            return False

    def change_password(self, user):
        try:
            user_id = user['user_id']
            pw = user['pw']
            db = self.client['kamc']
            collection = db['users']
            collection.update_one({'user_id': user_id}, {'$set': {'pw': pw}})
            return True
        except:
            return False


database_helper = DatabaseHelper()
school_list = database_helper.get_all_data_from_school_name()
