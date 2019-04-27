import urllib.request,json
from .models import User
# from app import app 

#Getting the api key
#api_key = None

#Getting the base url
base_url = None

def configure_request(app):
    global base_url #,api_key
    base_url = app.config['QUOTES_API_BASE_URL']
    #api_key = app.config['BLOG_API_KEY']

def get_quote(quote):
    '''
    funtion that gets the json response to the url request
    '''
    get_quote_url = base_url
    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = base_url

        # if get_quote_response['quote']:
            # quote_results_list = get_quote_response['quote']
            # quote_results = process_results(quote_results_list)
            
    return quote_results

def process_results(quote_list):
    '''
    function that processes results of the quote and returns a list of quotes
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        author = quote_item.get('author')

        quote_object = Quote(id,quote,author)
        quote_results.append(quote_object)

    return quote_results

