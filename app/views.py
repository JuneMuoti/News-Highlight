from flask import render_template
from app import app
from .request import get_article,get_source

@app.route('/')
def index():
    general_sources =get_source('general')
    
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,general=general_source,)

@app.route('/news/<int:news_id>')
def news(news_id):
    
    
