from app import db
from app.databases.postgresql.postgre_repository import Postgre_Repository
from app.databases.mongodb.mongo_repository import Mongo_Repository

mongo_repo = Mongo_Repository()
postgre_repo = Postgre_Repository(db)
