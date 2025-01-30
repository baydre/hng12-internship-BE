"""
This module contains the basic information about the intern.
"""
from flask import Blueprint, jsonify, Response
from datetime import datetime, timezone

# Create a blueprint for basic information
display_info = Blueprint('basic_info', __name__)

@display_info.route('/', methods=['GET'])
def get_basic_info():
    """ Return basic information in JSON format """
    basic_info = {
        "email": "baydreafrica@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/baydre/hng12-internship-BE/"
    }

    return jsonify(basic_info), 200