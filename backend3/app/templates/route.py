import os
from app.models.dbobject import app


template_folder = os.path.join(os.path.dirname(__file__), '')
app.template_folder = template_folder
