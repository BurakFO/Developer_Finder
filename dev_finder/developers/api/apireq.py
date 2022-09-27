from http.client import responses
from types import new_class
from xml.etree.ElementInclude import include
import requests
import urllib.request
import json

frontend = ["ruby","angular",""]
topic = "ruby"
page_numb = "1"
contents_URL = "https://api.github.com/search/repositories?q=topic:" + topic + "&per_page=100&page=" + page_numb

print(contents_URL)
response = requests.get(contents_URL)

content = dict(response.json()) # convert response.json ==>> dict. So We can search on dict.
items = content['items']

size = len(items)

a = 0
id_data = []
profile_url_data =[]
avatar_url_data = []

while a!=size: 
        if (items[a]['owner']['type'] == 'User'): #Only searching for users
        # print(items[a]['owner']['id'])  #Getting ID 
            id_data.append(items[a]['owner']['id']) #Write id to the list.
            profile_url_data.append(items[a]['owner']['html_url']) #Write url of profile to the list.
            avatar_url_data.append(items[a]['owner']['avatar_url']) #Write avatar url to the list.
            a=a+1

        else:
            a=a+1
i=0
while i!=size:
    print(id_data[i])
    print(avatar_url_data[i])
    print(profile_url_data)
    









