#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines the models and schemas of the API.
The Translation class represents the translation data which
is coming from the frontend and gets transmitted to the
Unbabel API.
The TranslationSchema class defines validation properties
used by Marschmallow to serialize and deserialize instances
of the Translation class.
"""

from marshmallow import fields, validate

from . import db, ma


class Translation(db.Model):
    """ Model class of a translation """

    __tablename__ = "translations"
    # primary key for the database
    id = db.Column(db.Integer, primary_key=True)
    # the original text which should be translated
    orig_text = db.Column(db.Text, nullable=False)
    # the translated tesxt
    trans_text = db.Column(db.Text, nullable=True)
    # identifier of the language the original text should be translated to.
    target_language = db.Column(db.String(2), nullable=False)
    # identifier of the language the original text should be translated to.
    source_language = db.Column(db.String(2), nullable=False)
    # current status of the translation.
    # 3 different statuses (requested, pending, translated)
    status = db.Column(db.String(10), nullable=False)
    # unique identifier which comes from the Unbabel API
    uid = db.Column(db.String(30), unique=True, nullable=True)

    def __init__(self, orig_text, trans_text, target_language, source_language,
                 status, uid):
        """ Initializes the Translation class """
        self.orig_text = orig_text
        self.trans_text = trans_text
        self.target_language = target_language
        self.source_language = source_language
        self.status = Translation.map_status(status)
        self.uid = uid

    @staticmethod
    def map_status(status):
        """ Maps the statuses of the Unbabel API to own defined statuses """
        new_status = ""
        if "new" in status:
            new_status = "requested"
        elif "translating" in status:
            new_status = "pending"
        elif "completed" in status:
            new_status = "translated"

        return new_status


class TranslationSchema(ma.Schema):
    """ Schema class for the Translation model class """

    id = fields.Integer(dump_only=True)
    orig_text = fields.String(required=True, validate=validate.Length(min=1))
    trans_text = fields.String(required=False, validate=validate.Length())
    target_language = fields.String(
        required=True, validate=validate.Length(min=2, max=2))
    source_language = fields.String(
        required=True, validate=validate.Length(min=2, max=2))
    status = fields.String(required=True, validate=validate.OneOf(
        ["requested", "pending", "translated"]))
    uid = fields.String(
        required=False, validate=validate.Length(min=10, max=10))
