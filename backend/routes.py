from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    all_pictures=[]
    for pictures in data:
        all_pictures.append(pictures)
    return all_pictures

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    for picture_by_id in data:
        if picture_by_id['id']== int(id):
            return jsonify(picture_by_id)
    return jsonify({'error': 'Not found'}), 404
    


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture/", methods=["POST"])
def create_picture():
    new_data = request.get_json()
    

    for picture in data:
        if picture['id'] == new_data['id']:
            return {"Message": "picture with id {picture['id']} already present"}
    
    data.append(new_data)
    return jsonify(new_data), 201


######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    pass

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    pass
