from enum import Enum
from app import db

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"

class Translation(db.Model):
    __tablename__ = "translations"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    target_language = db.Column(db.Enum(Language), nullable=False)
    source_language = db.Column(db.Enum(Language), nullable=False)
    uid = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, text, target_language, source_language, uid):
        self.text = text
        self.target_language = target_language
        self.source_language = source_language
        self.uid = uid

    def __repr__(self):
        return '<Translation %r>' % self.uid
    
    def serialize(self):
        return {
            'uid': self.uid, 
            'text': self.text,
            'target_language': self.target_language,
            'source_language':self.source_language
        }