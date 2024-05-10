#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
from api.v1.views.index import status


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

app_views.route('/status', methods=['GET'], strict_slashes=False)(status)
