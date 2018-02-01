# from app import app
import urllib.request,json
from .models import Article,Source

# Article = article.Article
# Source=sources.Source
api_key=None
base_url=None
source_url=None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url =app.config['NEWS_API_BASE_URL']
    source_url =app.config['SOURCES_API_BASE_URL']
# print('hi')
def get_source(category):
    get_source_url= source_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results
# print('hi')
def process_results(source_list):
    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        # print(id)
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category =source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')
        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)
    # print(source_results)
    return source_results
def get_article(id):
    get_article_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data =url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_article(article_results_list)
    # print(article_results_list)
    return article_results
    
def process_article(article_list):
    article_results =[]
    source_dictionary ={}
    for result in article_list:
        # We store the nested dictionary in source_id
        source_id = result['source']
        # We extract and store it in our source_dictionary
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        print(name)
        # print(id)
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            print(id)
            source_object = Article(id,
                                     name,
                                     title,
                                     description,
                                     url,
                                     urlToImage, publishedAt)
            article_results.append(source_object)

    return article_results



    return source_results







