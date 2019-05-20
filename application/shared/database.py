from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()


class Persistent:
    @classmethod
    def find(cls, **kwargs):
        return cls.query().filter_by(**kwargs).first()

    @classmethod
    def find_all(cls, **kwargs):
        return cls.query().filter_by(**kwargs).all()

    @classmethod
    def find_by_id(cls, object_id):
        return cls.find(id=object_id)

    @classmethod
    def query(cls):
        return db.session.query(cls)

    def save(self):
        db.session.add(self)

    def save_and_persist(self):
        self.save()
        db.session.commit()

    def rollback(self):
        db.session.rollback()
