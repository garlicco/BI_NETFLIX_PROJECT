from sqlalchemy import MetaData
from database import engine, get_db,Base 
from models import imdb_ratings, netflix_credits, netflix_library, movies_revenues, engagement_report #only create the first 4 dimensions
import psycopg2
import json, io, pandas as pd

###########################Start main.py and create the database in postgreSQL##########################################

def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print('Debugging') #debugging to see if starting the file works

###########################Loading data into postgreSQL########################################################

def load_data(csv_file, table_name):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, engine, if_exists='append',
              index=False, chunksize=1000)
if __name__ == '__main__':
    main()
    load_data('new_data/new_imdb_ratings.csv','imdb_ratings')
    load_data('new_data/new_netflix_library_credits.csv','netflix_credits')
    load_data('new_data/new_movies_revenues.csv','movies_revenues')
    load_data('new_data/new_netflix_library.csv','netflix_library')
    load_data('new_data/new_netflix_engagement_report.csv','fact_netflix_engagement')
    print("Data added to postgresql")



