import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/newest")

web_page = BeautifulSoup(response.text,'html.parser')
articles= web_page.find_all(class_="titleline")
articles_final = web_page.find_all('a')

article_text = []
article_link = []

##putting all link and text into two arrays

for article_tag in articles:
    article_text.append(article_tag.getText())
    article_link.append(article_tag.find('a').get('href'))
   

scores = web_page.find_all(class_="score")

scores_text = [int(score.getText().split()[0]) for score in scores]

best_articles ={}
best_link={}

for x, y in enumerate(article_text):
    best_articles[scores_text[x]] = y
    best_link[y] = article_link[x]


##most rated article

largest_value= max(scores_text)

#for x in articles:
#    print(x.find('a').get('href'))

print("Article:", best_articles[largest_value], "score:",largest_value,"link",best_link[best_articles[largest_value]])