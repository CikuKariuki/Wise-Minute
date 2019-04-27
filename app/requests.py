import urllib.request,json
from .models import User

#Getting the api key
#api_key = None

#Getting the base url
base_url = None

def configure_request(app):
    global base_url #,api_key
    base_url = app.config['QUOTES_API_BASE_URL']
    #api_key = app.config['BLOG_API_KEY']
    