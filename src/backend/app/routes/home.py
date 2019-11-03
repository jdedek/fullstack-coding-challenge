from flask import current_app as app
from flask import render_template, request, json, Response
from flask_restful import Resource
from app.models.translation import Translation, TranslationSchema
from app.models import db

translation_schema = TranslationSchema()
translations_schema = TranslationSchema(many=True)

class TranslationRessource(Resource):
    def get(self):
        translations = Translation.query.all()
        translations = translations_schema.dump(translations).data
        return {'status': 'success', 'data': translations}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = translation_schema.load(json_data)
        if errors:
            return errors, 422
        translation = Translation.query.filter_by(orig_text=data['orig_text']).first()
        if translation:
            return {'message': 'Translation already exists'}, 400
        translation = Translation(
            orig_text=json_data['orig_text'],
            target_language=json_data['target_language'],
            source_language=json_data['source_language'],
            status=json_data['status']
        )

        db.session.add(translation)
        db.session.commit()

        result = translation_schema.dump(translation).data

        return { "status": 'success', 'data': result }, 201
    
    def delete(self, translation_id):
        translation = Translation.query.filter_by(id=translation_id).delete()
        if not translation:
            return 422

        db.session.commit()
        result = translation_schema.dump(translation).data

        return { "status": 'success', 'data': result}, 204