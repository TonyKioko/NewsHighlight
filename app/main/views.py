from flask import render_template,request
from . import main
from ..requests import get_sources,get_articles,get_headline_articles
from ..models import Source,Article


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general = get_sources('general')
    business = get_sources('business')
    sports = get_sources('sports')
    technology = get_sources('technology')
    science = get_sources('science')
    health = get_sources('health')
    entertainment = get_sources('entertainment')
    
    

    title = 'News Now'
    return render_template('index.html',title=title,general=general,business = business,sports = sports,technology = technology,health=health,science=science,entertainment = entertainment)

@main.route('/articles/<id>')
def articles(id):
    '''
    view page function that returns the source articles and its data
    '''
    articles = get_articles(id)
    title = 'News Now'


    return render_template('articles.html', articles=articles, title=title)

@main.route('/topheadlines/<en>')
def topheadlines(en):
    '''
    view page function that returns the topheadlines by langauge
    '''
    headlines = get_headline_articles('en')
    title = 'News Now'


    return render_template('topheadlines.html', headlines=headlines, title=title)

    
  







# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     news_sources = get_sources('sources')
#     title = 'News Now'
#     return render_template('index.html',news_sources=news_sources,title=title)

