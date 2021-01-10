from sqlalchemy import Enum
from sqlalchemy.orm import relationship

from casehub.db import db
from casehub.steps.schemas import StepType


class StepModel(db.Model):
    __tablename__ = 'steps'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode())
    text = db.Column(db.UnicodeText())
    type = db.Column(Enum(StepType))
    place = db.Column(db.Integer())
    case_id = db.Column(db.Integer(), db.ForeignKey('cases.id'), nullable=False)
    case = relationship("CaseModel")
