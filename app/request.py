from app import app
import urllib.request,json
from .models import article

Article = article.Article
api_key = app.config['NEWS_API_KEY']
base_url =app.config["NEWS_API_BASE_URL"]

def get_article(general):
    get_article_url = base_url.format(general,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data =url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results
def process_results(article_list):
    article_results =[]
    for article_item in article_list:
        
        author = article_item.get('author')
        title =article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        if url:
            article_object = Article(author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)


    return article_results



