from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id=news_id)