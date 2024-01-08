import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

def main():
    response = requests.get(URL)
    website_html = response.text

    soup = BeautifulSoup(website_html, 'html.parser')
    all_movies = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
    movie_titles = [movie.getText() for movie in all_movies]
    #movies_ordered = movie_titles[::-1]
    movie_titles.reverse()

    with open('movies.txt', mode='w') as file:
        for movie in movie_titles:
            file.write(f'{movie}\n')



if __name__ == '__main__':
    main()