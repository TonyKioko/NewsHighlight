from flask import render_template,request
from app import app
from .requests import get_sources,get_articles


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = get_sources('general')
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    business = get_sources('business')
    health = get_sources('health')
    science = get_sources('science')

    title = 'News Now'
    return render_template('index.html',title=title,business = business,health=health,science=science,sports = sports, technology = technology,entertainment = entertainment ,general=general)

@app.route('/news/<id>')
def news(id):
    '''
    view page function that returns the news articles and its data
    '''
    articles = get_articles(id)
    title = 'News Now'

    return render_template('news.html', articles=articles, title=title)
    







# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     news_sources = get_sources('sources')
#     title = 'News Now'
#     return render_template('index.html',news_sources=news_sources,title=title)

