import pandas as pd
import requests
from bs4 import BeautifulSoup 
import numpy as np
import csv
import random

class Movies_now:
    def scraping_function():
        url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
        response = requests.get(url)
        response
        soup = BeautifulSoup(response.content,'html.parser')
        # print(soup)
        movie_name = []
        year = []
        time = []
        rating = []
        metascore = []
        votes = []
        gross = []

        movie_data = soup.findAll('div', attrs={'class' : 'lister-item mode-advanced'})

        # print(movie_data)

        for store in movie_data:
            name = store.h3.a.text
            movie_name.append(name)
            year_of_release = store.h3.find ('span',class_ = 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
            year.append(year_of_release)
            runtime = store.p.find('span',class_ = 'runtime').text.replace(' min','')
            time.append(runtime)
            rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n','')    
            rating.append(rate)

        # print(year_of_release)
        # count=np.count_nonzero(movie_name)
        # print(count)
        movie_DF = pd.DataFrame({'Name of movie' : movie_name,'Year of release' : year, 'Watch time' : time, 'Movie rating' : rating})
        print(movie_DF)
        movie_DF.to_csv('movies_list.csv')    
    
    def reader():
        dd = open('movies_list.csv')
        for data in dd:
            print(data)    
    
    def welcome_page():       
        print(f'''welcome to my movie suggestion project it will help you get a movie from a particular website
              now I Listed movie below
              {o.reader()}
              and do you need to some random movie from the website just press "N" 
              or press " Y " to continue ''')
        choice=input('Enter your input : ')          
        if choice == "y" or choice =='Y':
            print('Enter the Sireal No to get the movie ')
            movie_nu = int(input('Enter your input : '))
            o.movie_selection(movie_nu)
            
        elif choice == "N" or choice == 'n':
            o.random_movie()
            
        else:
            print('Wrong Input ')
    
    def movie_selection(num):
         with open('movies_list.csv') as f:
            d = csv.reader(f)
            header, l = next(d), list(d)
            print(f'''I get your prefernce movie {l[num]}
                  Do you like the movie Press "y"
                  didn't like the movie press "N" to pic movie again''')
            like=input('Enter your input : ')
            if like == 'y' or like=='Y':
                print('Enjoy the movie !')
                print(r)
            elif like == 'N' or like == 'n':
                print('reproccesing....')
                print('Come back again user')
                           
    
    def random_movie():
            with open('movies_list.csv') as f:
                r = csv.reader(f)
                header, l = next(r), list(r)
                r = random.choice(l)
                print(r)
            print('Did like this movie press "Y" to cotinue ')
            print("Don't you like press 'N' to run again")
            like=input('Enter your input : ')
            if like == 'y' or like=='Y':
                print('Enjoy the movie !')
                print(r)
            elif like == 'N' or like == 'n':
                print('reproccesing....')
                o.random_movie()
            
o=Movies_now
while True:
    o.welcome_page()
    break
else:
    print ('Error occored on your input')