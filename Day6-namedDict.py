from collections import defaultdict, namedtuple, Counter, deque
import csv
import os.path
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'data/movies.csv'

if os.path.isfile(movies_csv):
    print('file has been downloaded')
else:
    urlretrieve(movie_data, movies_csv)

# lets start with a named tuple
Movie = namedtuple('Movie', 'title year score')

# Parse the CSV

def get_movies_by_director(data=movies_csv):
    #here you need to define the type for your default dict (list)
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors

directorsM = get_movies_by_director()