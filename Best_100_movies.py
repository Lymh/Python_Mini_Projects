import requests
from bs4 import BeautifulSoup

response =  requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = BeautifulSoup(response.text,'html.parser')

List_Best_Movies = web_page.find_all(class_="title")


List_Best_Movies_Text= [title_movies.getText() for title_movies in List_Best_Movies]

with open("movies.txt",mode="w",encoding='utf-8') as file:
    for movie in List_Best_Movies_Text:
        file.write(f'{movie}\n')