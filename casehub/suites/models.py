from sqlalchemy.orm import relationship

from casehub.db import db


class SuiteModel(db.Model):
    __tablename__ = 'suites'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode())
    project = relationship('ProjectModel')
    project_id = db.Column(db.Integer(), db.ForeignKey('projects.id'))
