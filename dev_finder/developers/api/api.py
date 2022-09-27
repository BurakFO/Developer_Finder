from http.client import responses
import requests
import urllib.request
import json

# contents = urllib.request.urlopen("https://api.github.com/search/repositories?q=topic:ruby&per_page=100&page=1").read()


# contents_json = json.loads(contents)
# item = contents_json['items']

# # for i in item:
# #      a=i['owner']
# #      print(a)
# ownerArray = []
# array = [{'anahtar': 'sonuc', 'id':1533},{'anahtar': 'kapi', 'id':15}]

# k=0
# for i in item: 
#     ownerArray[k] = i['owner']
#     k=k+1

# print(array[0]['anahtar'])
    
# #    while (i['owner']) == 'User':
    
        

   
   
   











# pageNumber = [1,2,3]

# class Github:
#     def __init__(self):
#         self.api_url = 'https://api.github.com'

#     # def getDeveloper (self, framework):  #getDeveloper takes framework parameter. So we can make a decision about developers.
#     #     response = requests.get(self.api_url+'/search/repositories?q=topic:'+ framework)
#     #     return response

#     def getDeveloper (self, framework):
        
#         response = requests.get(self.api_url+'/search/repositories?q=topic:'+ framework+'&per_page=100&page='+pageNumber[i])
#         return response.json()

# github = Github()

# print(type(github.getDeveloper('ruby')))





# chose = input("ruby yaz ve ruby'e git\n")

# if chose == 'ruby':
#     github.getDeveloper(chose)
#     print()


