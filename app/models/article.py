class Article:
    '''
    Article class to define Article objects
    '''
    def __init__(self,id,name,author,title,description,url,image,date):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date