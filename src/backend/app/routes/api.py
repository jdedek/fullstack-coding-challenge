#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines the API methods like GET, POST and DELETE.
The TranslationRessource class contains these methods and
inherrits from the Flask-Restufl Resource class where these
methods are pre-defined.

More informations about Flask-Restful:
https://flask-restful.readthedocs.io/en/latest/quickstart.html#resourceful-routing
"""

import os
import requests

from flask import current_app as app
from flask import render_template, request, json, Response
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy import exc

from app.models import db
from app.models.translation import Translation, TranslationSchema

# instanciate the Schema for validation and serialization
translation_schema = TranslationSchema()
translations_schema = TranslationSchema(many=True)

# gets the API key, username and url of the Unbabel API
# from enviroment variables
unbabel_username = os.environ["UNBABAEL_USERNAME"]
unbabel_api_key = os.environ["UNBABEL_API_KEY"]
unbabel_api_url = os.environ["UNBABEL_API_URL"]

# specific header for the Unbabel API
headers = {'Authorization': 'ApiKey {}:{}'.format(
    unbabel_username, unbabel_api_key), 'content-type': 'application/json'}


class TranslationRessource(Resource):
    """ Model class of a translation """

    def get(self):
        """ handles GET requests from the frontend app """
        # get all existing translations from the database
        translations = Translation.query.all()

        for translation in translations:
            # gets the current data for every translation the db from
            # the Unbabel API
            # HACK with more datasets this would be a bottleneck. But since the
            # fullstack-challenge account is floded with data I wanted just the
            # translations wich were created by this application
            try:
                unbabel_res = requests.get(
                    unbabel_api_url+str(translation.uid)+"/", headers=headers)
            except ValidationError as err:
                app.logger.error(err.messages)
                return err.messages, 422
            # checks if the properties are availible and saves them in the
            # current instance of the Translation class.
            json_data = unbabel_res.json()
            if json_data:
                if 'target_language' in json_data.keys():
                    translation.target_language = json_data['target_language']
                if 'source_language' in json_data.keys():
                    translation.source_language = json_data['source_language']
                if 'status' in json_data.keys():
                    translation.status = Translation.map_status(
                        json_data['status'])
                if 'uid' in json_data.keys():
                    translation.uid = json_data['uid']
                if 'text' in json_data.keys():
                    translation.orig_text = json_data['text']
                if 'translatedText' in json_data.keys():
                    translation.trans_text = json_data['translatedText']

                # deletes the old db entry and saves it again
                db.session.delete(translation)
                db.session.add(translation)

                try:
                    db.session.commit()
                except exc.SQLAlchemyError as err:
                    app.logger.error(err.messages)
                    return err.messages, 500

        # serializes the translations into JSON data
        translations = translations_schema.dump(translations).data
        return {'status': 'success', 'data': translations}, 200

    def post(self):
        """ handles POST requests from the frontend app """
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        try:
            data = translation_schema.load(json_data)
        except ValidationError as err:
            app.logger.error(err.messages)
            return err.messages, 422

        try:
            unbabel_res = requests.post(unbabel_api_url, headers=headers, json={
                                        'text': json_data['orig_text'],
                                        'target_language': json_data['target_language'],
                                        'source_language': json_data['source_language']})
        except requests.exceptions.RequestException as err:
            app.logger.error(err.messages)
            return err.messages, 422

        if unbabel_res:
            unbabel_json_data = unbabel_res.json()
            # create new Transalation instance from Unbabel API JSON
            if unbabel_json_data:
                translation = Translation(
                    orig_text=unbabel_json_data['text'],
                    trans_text="",
                    target_language=unbabel_json_data['target_language'],
                    source_language=unbabel_json_data['source_language'],
                    status=unbabel_json_data['status'],
                    uid=unbabel_json_data['uid']
                )
                # save translation in database
                db.session.add(translation)
                try:
                    db.session.commit()
                except exc.SQLAlchemyError as err:
                    app.logger.error(err.messages)
                    return err.messages, 500

            # serializes the translations into JSON data
            result = translation_schema.dump(translation).data
            return {"status": 'success', 'data': result}, 201

    def delete(self, uid):
        """ handles DELETE requests from the frontend app """
        # fetch the translation with the given uid from db and deletes it.
        translation = Translation.query.filter_by(uid=uid).delete()

        if not translation:
            return 422

        try:
            requests.delete(unbabel_api_url+uid+"/",
                            headers=headers)
        except requests.exceptions.RequestException as err:
            app.logger.error(err.messages)
            return err.messages, 422

        # save changes in database
        try:
            db.session.commit()
        except exc.SQLAlchemyError as err:
            app.logger.error(err.messages)
            return err.messages, 500

        # give back the deleted translation
        result = translation_schema.dump(translation).data
        return {"status": 'success', 'data': result}, 204
