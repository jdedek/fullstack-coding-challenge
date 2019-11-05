#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module tests the backend application
"""

import pytest

from app import create_app

@pytest.fixture
def app():
    app = create_app(config_name="testing")
    return app


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c

def test_post_translation(client):
    """Test API can create a translation (POST request)"""
    translation = {"orig_text":"This is a test",
                           "target_language":"es",
                           "source_language":"en",
                           "status":"requested"}

    response = client.post("/api/translations/", json=translation)
    result= response.get_json()
    assert result["data"]["status"] == translation["status"]
    assert result["data"]["target_language"] == translation["target_language"]
    assert result["data"]["source_language"] == translation["source_language"]
    assert result["data"]["orig_text"] == translation["orig_text"]
    assert response.status_code == 201


def test_get_translations(client):
    """Test API can get a translations (GET request)"""

    get_response = client.get("/api/translations/")
    assert get_response.status_code == 200


def test_delete_translation(client):
    """Test API can delete a translations (DELETE request)"""
    translation = {"orig_text":"This is another another test",
                           "target_language":"es",
                           "source_language":"en",
                           "status":"requested"}

    post_response = client.post("/api/translations/", json=translation)
    post_result = post_response.get_json()
    try:
        uid = post_result["data"]["uid"]
    except KeyError:
        pass
    del_response = client.delete("/api/translations/"+uid+"/")
    assert del_response.status_code == 404
