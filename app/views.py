from flask import render_template
from app import app
from .request import get_article,get_source

@app.route('/')
def index():
    general_sources =get_source('general')
    
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,general=general_source,)

@app.route('/news/<id>')
def news(id):
    articles =get_article(id)
    title= "Enjoy the news"
    return render_template('news.html',articles=articles,title=title)
    
    
    
