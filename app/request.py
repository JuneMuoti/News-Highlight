from app import app
import urllib.request,json
from .models import article

Article = artic.Article
Source=sources.Source

api_key = app.config['NEWS_API_KEY']
base_url =app.config['NEWS_API_BASE_URL']
source_url =app.config['SOURCES_API_BASE_URL']

def get_article(id):
    get_article_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data =url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results
def process_article(article_list):
    article_results =[]
    source_dictionary ={}
    for article_item in article_list:
        source_id=article_item['source']
        source_dictionary['id']=source_id['id']
        source_dictionary['name']=source_id['name']
        id=source_dictionary['id']
        name= source_dictionary['name']
        print(name)
        author = article_item.get('author')
        title =article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        if urlToImage:
            source_object = Article(id,name,author,title,description,url,urlToImage,publishedAt)
            article_results.append(source_object)


    return article_results
def get_source(category):
    get_source_url =source_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.reaD()
        get_source_response = json.loads(get_source_data)

        source_results = None
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category =source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')
        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results







