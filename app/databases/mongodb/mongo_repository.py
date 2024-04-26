from pymongo import MongoClient


class Mongo_Repository:
    def __init__(self, host: str = 'localhost',
                 port: int = 27017,
                 db_name: str = "films",
                 collection: str = "all_films"):
        self._client = MongoClient(f'mongodb://{host}:{port}')
        self._collection = self._client[db_name][collection]

    def create_film(self, film: str):
        try:
            if self._collection.find_one({"title": film.get('title')}) is None:
                self._collection.insert_one(film)
                print(f"Added new film: {film.get('title')}")
            else:
                print(f"Film: {film.get('title')} in collection")
        except Exception:
            print("[create_film] Some problem...")

    def get_all_films(self):
        try:
            data = self._collection.find()
            print("Get all films")
            return data
        except Exception:
            print("[get_all] Some problem...")
