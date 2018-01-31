from flask import render_template,request,redirect,url_for
from . import main
from .request import get_source,get_article


@main.route('/')
def index():
    general_sources =get_source('general')
    title = 'Welcome to the best news Feed app ever'
    return render_template('index.html',title=title,general=general_sources,)

@main.route('/news/<id>')
def news(id):
    articles =get_article(id)
    title= "Enjoy the news"
    return render_template('news.html',articles=articles,title=title)

    
    
