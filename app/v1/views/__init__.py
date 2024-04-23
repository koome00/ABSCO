from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/absco/")

from app.v1.views.routes import *