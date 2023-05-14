import requests
from bs4 import BeautifulSoup
data=requests.get("https://www.timeout.com/film/the-100-best-bollywood-movies-the-list").text

movie_data=BeautifulSoup(data,"html.parser")
movie_titles=movie_data.find_all(name="h3",class_="_h3_cuogz_1")

for i in range(len(movie_titles)):
    with open("./recommended_movies.txt","a") as recommended_movies:
        content=movie_titles[len(movie_titles)-i-1].getText().split()
        item=content[0]+" "+content[1]+" "+content[2]
        recommended_movies.write(f"{item}\n")

    

