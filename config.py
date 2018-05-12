import os
class Config:
    '''
    General configuration for the parent class
    '''
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={general}&apiKey={}'
    EVERYTHING_LOCATION_BASE_URL = 'https://newsapi.org/v2/everything?sources={reuters}&apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,bloomberg,engadget,espn,fortune,al-jazeera-english,cnn,independent&pageSize={30}&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={30}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig:
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig:
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}