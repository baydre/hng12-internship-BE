"""
This module contains the basic information about the intern.
"""
from flask import Blueprint, Response
from datetime import datetime, timezone
import json

# Create a blueprint for basic information
display_info = Blueprint('basic_info', __name__)

@display_info.route('/', methods=['GET'])
def get_home():
    """ Return a welcome message """
    message = "Welcome to Baydre's Stage 0 Task for HNG12 Internship!"
    return Response(message, mimetype="text/plain")

@display_info.route('/basic-info', methods=['GET'])
def get_basic_info():
    """ Return basic information in JSON format """
    basic_info = {
        "email": "baydreafrica@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/baydre/hng12-internship-BE/stage0"
    }

    json_output = json.dumps(basic_info, indent=4)
    return Response(json_output, mimetype="application/json")