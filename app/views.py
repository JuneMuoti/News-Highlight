from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    general_sources = get_sources()
    print(general_sources)
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,general=general_sources)

@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id=news_id)