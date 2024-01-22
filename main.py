from sqlalchemy import MetaData
from database import engine, get_db,Base
from models import *

import psycopg2
import json, io, pandas as pd

###########################Start main.py and create the database in postgreSQL##########################################

def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print('Debugging') #debugging to see if starting the file works

###########################Loading data into postgreSQL########################################################
def load_data(csv_file, table_name, foreign_key_columns=None):
    df = pd.read_csv(csv_file)

    df.to_sql(table_name, engine, if_exists='append', index=False, chunksize=100)
if __name__ == '__main__':
    main()
    

    load_data('new_data/new_revenues.csv', 'revenues')
    print("revenue data added to postgresql")
    load_data('new_data/new_regions.csv', 'regions')
    print("region data added to postgresql")
    load_data('new_data/new_engagement.csv', 'engagement')
    print("engagement added to postgresql")

    load_data('new_data/new_credits.csv', 'credits')
    print("credits data added to postgresql")

    load_data('new_data/new_genres.csv', 'genres')
    print("genres data added to postgresql")

    load_data('new_data/new_imdb_ratings.csv', 'fact_imdb_ratings')
    print("imdb_ratings added to postgresql")



