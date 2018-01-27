from flask import render_template
from app import app
from .request import get_article

@app.route('/')
def index():
    general_news = get_article('general')
    # print(general_news)
    business_news=get_article('business')
    health_news=get_article('health')
    
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,general=general_news,business=business_news,health=health_news)

@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id=news_id)