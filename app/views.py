from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources('sources')
    title = 'News Now'
    return render_template('index.html',news_sources=news_sources,title=title)

