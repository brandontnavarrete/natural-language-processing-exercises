import pandas as pd
import numpy as np
import os
from os import path

import requests
from requests import get

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Codeup Data Science'} 



# function
def get_blog_articles(urls):
    # Initialize an empty list to store the dictionaries
    articles = []

    for url in urls:
        # Send a GET request to the URL and store the response
        response = requests.get(url,headers = headers)
    
        # Parse the response content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Extract the title and content of the article
        title = soup.title.string
        divs = soup.find('div', class_='entry-content')
        
        # Loop through the divs and extract the text content
        content = []
        for div in divs:
            text = div.text
        
            content.append(text)
        
        # Create a dictionary to store the title and content
        article_dict = {'title': title, 'content': content}
    
        # Append the dictionary to the list of articles
        articles.append(article_dict)
    
    # Return the list of dictionaries
    return articles
    


def get_article_text():
    # if we already have the data, read it locally
    if path.exists('article.txt'):
        with open('article.txt') as f:
            return f.read()

    # otherwise go fetch the data
    url = 'https://codeup.com/data-science/math-in-data-science/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article = soup.find('div', id='main-content')

    # save it for next time
    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text


# function
def get_new_article_business():
    
    # Initialize an empty list to store the dictionaries
    articles = []
    url = 'https://blog.inshorts.com/2018/12/19/56-indians-are-satisfied-with-the-current-government-inshorts-pulse-of-the-nation-poll/'
    
    
    # Send a GET request to the URL and store the response
    response = requests.get(url,headers = headers)
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title and content of the article
    title = soup.title.string
    content = soup.find('div', class_='entry-content').text
    
    # Create a dictionary to store the title and content
    article_dict = {'title': title, 'content': content, 'category':'business'}
    
    # Append the dictionary to the list of articles
    articles.append(article_dict)
    
    # Return the list of dictionaries
    return articles



# function
def get_new_article_sports():
    
    # Initialize an empty list to store the dictionaries
    articles = []
    url = 'https://blog.inshorts.com/2021/07/23/68-confident-india-will-improve-performance-at-tokyo-olympics-compared-to-rio-public-ki-awaaz-poll/'
    
    
    # Send a GET request to the URL and store the response
    response = requests.get(url,headers = headers)
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title and content of the article
    title = soup.title.string
    content = soup.find('div', class_='entry-content').text
    
    # Create a dictionary to store the title and content
    article_dict = {'title': title, 'content': content, 'category':'sports'}
    
    # Append the dictionary to the list of articles
    articles.append(article_dict)
    
    # Return the list of dictionaries
    return articles

# function
def get_new_article_tech():
    
    # Initialize an empty list to store the dictionaries
    articles = []
    url = 'https://blog.inshorts.com/2021/01/14/47-find-whatsapps-updated-privacy-policy-unacceptable-says-inshorts-poll/'
    
    # Send a GET request to the URL and store the response
    response = requests.get(url,headers = headers)
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title and content of the article
    title = soup.title.string
    content = soup.find('div', class_='entry-content').text
    
    # Create a dictionary to store the title and content
    article_dict = {'title': title, 'content': content, 'category':'tech'}
    
    # Append the dictionary to the list of articles
    articles.append(article_dict)
    
    # Return the list of dictionaries
    return articles

# function
def get_new_article_ent():
    
    # Initialize an empty list to store the dictionaries
    articles = []
    url = 'https://blog.inshorts.com/2021/10/08/festivities-in-the-air-but-indians-still-cautious-with-money-public-app-survey/'
    
    # Send a GET request to the URL and store the response
    response = requests.get(url,headers = headers)
    
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title and content of the article
    title = soup.title.string
    content = soup.find('div', class_='entry-content').text
    
    # Create a dictionary to store the title and content
    article_dict = {'title': title, 'content': content, 'category':'entertainment'}
    
    # Append the dictionary to the list of articles
    articles.append(article_dict)
    
    # Return the list of dictionaries
    return articles

