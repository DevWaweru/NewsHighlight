class Sources:
    '''
    Sources class that defines source objects
    '''
    def __init__(self,id,name,description,url,category,country):
        '''
        Function that initiates the sources class
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class Articles:
    '''
    Article class that defines the article objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt