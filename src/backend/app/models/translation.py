from enum import Enum
from marshmallow import Schema, fields, pre_load, validate
from . import db, ma

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"

class Status(Enum):
    REQUESTED = "new"
    PENDING = "translating"
    TRANSLATED = "completed"

class Translation(db.Model):
    __tablename__ = "translations"
    id = db.Column(db.Integer, primary_key=True)
    orig_text = db.Column(db.Text, nullable=False)
    trans_text = db.Column(db.Text, nullable=True)
    target_language = db.Column(db.String(2), nullable=False)
    source_language = db.Column(db.String(2), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    uid = db.Column(db.String(30), unique=True, nullable=True)

    def __init__(self, orig_text, target_language, source_language, status):
        self.orig_text = orig_text
        self.target_language = target_language
        self.source_language = source_language
        self.status = status

class TranslationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    orig_text = fields.String(required=True, validate=validate.Length(1))
    trans_text = fields.String(required=False, validate=validate.Length(1))
    target_language = fields.String(required=True, validate=validate.Length(1))
    source_language = fields.String(required=True, validate=validate.Length(1))
    status = fields.String(required=True, validate=validate.Length(1))
    uid = fields.String(required=False, validate=validate.Length(1))