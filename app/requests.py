from app import app
import urllib.request
import json
# from .models import Source
from .models import source,article

Source = source.Source
Article = article.Article

# Getting api key
# api_key = app.config['NEWS_API_KEY']
api_key='3f7ad7ad6ae546a28feead545feea3c4'


# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(source):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = "https://newsapi.org/v2/sources".format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

        # if name:
        #     source_object = Source(id,name,description,url,category,language,country)
            # source_results.append(source_object)
        #    

    return source_results
