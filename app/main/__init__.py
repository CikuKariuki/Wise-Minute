from flask import Blueprint
main = Blueprint('main',__name__) #this initialises the blueprint __name__ helps us locate the blueprint
from . import views, errors #we import these to avoid circular dependencies


