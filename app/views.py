from flask import render_template
from app import app
from .request import get_article

@app.route('/')
def index():
    top_headlines = get_article('general')
    print(top_headlines)
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,trending=top_headlines)

@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id=news_id)