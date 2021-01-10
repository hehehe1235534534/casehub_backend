from sqlalchemy.orm import relationship

from casehub.db import db


class CaseModel(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode())
    description = db.Column(db.UnicodeText())
    suite = relationship('SuiteModel')
    suite_id = db.Column(db.Integer(), db.ForeignKey('suites.id'))
