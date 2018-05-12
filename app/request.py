import urllib.request, json
from .models import Sources,Articles

api_key = None
sources_url = None

def configure_request(app):
    global api_key, sources_url
    api_key = app.config['NEWS_API_KEY']
    # api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_per_source_url = app.config['EVERYTHING_LOCATION_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])
    
    return sources_results

def process_results(sources_list):
    '''
    Function that processes the json results
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')

        if url:
            source_object = Sources(id,name,description,url,category,country)
            sources_results.append(source_object)
    
    return sources_results

def get_articles(id):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_per_source_url.format(id,api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])
        
    return articles_location_results