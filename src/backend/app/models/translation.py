from enum import Enum
from . import db

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
    target_language = db.Column(db.Enum(Language), nullable=False)
    source_language = db.Column(db.Enum(Language), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    uid = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, orig_text, trans_text, target_language, source_language, status, uid):
        self.orig_text = orig_text
        self.trans_text = trans_text
        self.target_language = target_language
        self.source_language = source_language
        self.status = status
        self.uid = uid

    def __repr__(self):
        return '<Translation %r>' % self.uid
    
    def serialize(self):
        return {
            'uid': self.uid, 
            'orig_text': self.orig_text,
            'trans_text': self.trans_text,
            'target_language': self.target_language,
            'source_language':self.source_language,
            'status': self.status
        }