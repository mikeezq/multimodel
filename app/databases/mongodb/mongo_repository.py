import os

from pymongo import MongoClient
from app.s3.s3 import get_presigned_url


class Mongo_Repository:
    def __init__(self, host: str = 'localhost',
                 port: int = 27017,
                 db_name: str = "shows",
                 collection: str = "all_shows"):
        self._client = MongoClient(f'mongodb://{host}:{port}')
        self._collection = self._client[db_name][collection]

    def create_show(self, show: dict):
        try:
            if self._collection.find_one({"title": show.get("title")}) is None:
                self._collection.insert_one(show)
                print(f"Added new show: {show}")
        except Exception:
            print("[create_show] Some problem...")

    def get_show_link(self, title: str):
        try:
            show = self._collection.find_one({"title": title})
            return show.get('link')
        except Exception:
            print("No show image with such title")

    def get_all_shows(self):
        try:
            data = self._collection.find()
            print("Get all shows")
            return data
        except Exception:
            print("[get_all] Some problem...")

    def init_db(self):
        media_dir = os.path.join(os.getcwd(), "static", "img", "shows")

        for flag in os.listdir(media_dir):
            basename = os.path.splitext(os.path.basename(flag))[0]
            self.create_show({"title": basename, "link": get_presigned_url(flag)})
        print("mongo up to date")
